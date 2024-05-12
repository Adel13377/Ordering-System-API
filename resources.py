from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask import render_template, request, jsonify, send_file
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import stripe
from models import OrderModel, ProductModel, db



# Request parser for order endpoint
order_parser = reqparse.RequestParser()
order_parser.add_argument('product_id', type=int, required=True, help="Product ID is required")
order_parser.add_argument('quantity', type=int, required=True, help="Quantity is required")
order_parser.add_argument('email', type=str, required=True, help="Email is required")


# Resource fields for product/order
product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'quantity': fields.Integer
}
order_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'total_price': fields.Float,
    'quantity': fields.Integer,
    'email': fields.String
}



#Add product / Retrieve all products / Retrieve specific product info / Delete product
class ProductList(Resource):
    @marshal_with(product_fields)
    def get(self, product_id=None):  # Accept product_id as a parameter
        if product_id is not None:
            result = ProductModel.query.filter_by(id=product_id).first()
            if result is None:
                abort(404, message='Product not found')
            return result
        else:
            result = ProductModel.query.all()
            return result
    
    @marshal_with(product_fields)
    def post(self):
        # Parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('price', type=float, required=True, help='Price is required')
        parser.add_argument('quantity', type=int, required=True, help='Quantity is required')
        args = parser.parse_args()    
        new_product = ProductModel(name=args['name'], price=args['price'], quantity=args['quantity'])
        
        db.session.add(new_product)
        db.session.commit()
        
        return new_product, 201

    def delete(self, product_id):
        product = ProductModel.query.get(product_id)
        if product is None:
            abort(404, message='Product not found')

        db.session.delete(product)
        db.session.commit()

        return {'message': 'Item deleted successfully'}, 200

    
#Make an order ( Includes mockpayment gateway / Email confirmation )
class Order(Resource):
    def post(self):
        args = order_parser.parse_args()
        product_id = args['product_id']
        quantity = args['quantity']
        email = args['email']        
        product = ProductModel.query.filter_by(id=product_id).first()
        if product is None:
            return {'message': 'Product not found'}, 404
        
        # Check if requested quantity is available
        if quantity > product.quantity:
            return {'message': 'Insufficient stock for the requested quantity'}, 400
        
        total_price = quantity * product.price
        
        try:
            # Create a PaymentIntent with Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=total_price*100,
                currency="usd",
                payment_method_types=["card"],
                metadata={"integration_check": "accept_a_payment"},
            )
            cust_id = 'pi_'+str(payment_intent['client_secret']).split('_')[1]
            result = stripe.PaymentIntent.confirm(cust_id,payment_method="pm_card_visa")
            

            new_order = OrderModel(product_id=product_id, quantity=quantity, total_price=total_price, email=email)
            
            db.session.add(new_order)
            product.quantity -= quantity
            db.session.commit()

            email_address = email
            email_subject = "Thanks for buying from our Service!"
            email_html = render_template('email.html', product=product.name, quantity=quantity, total_price=total_price)

            sender_email = 'salmakhaled76543@gmail.com'
            sender_password = 'wsvr guox nsov rbny'
            receiver_email = email_address
            
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = email_subject
            message.attach(MIMEText(email_html, 'html'))

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()

            except Exception as e:
                return str(e)
                    
            
            # Return response with client secret for front-end payment confirmation
            return {
                'client_secret': payment_intent.client_secret,
                'order_details': {
                    'product_id': product_id,
                    'product_name': product.name,
                    'product_price': product.price,
                    'quantity': quantity,
                    'total_price': total_price,
                    'timestamp': datetime.now().isoformat()
                }
            }, 201
        
        except stripe.error.StripeError as e:
            return {'error': str(e)}, 400

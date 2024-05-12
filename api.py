from flask import Blueprint
from flask_restful import Api
from resources import ProductList, Order

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)


api.add_resource(ProductList, '/products', '/products/<int:product_id>')
api.add_resource(Order, '/order')

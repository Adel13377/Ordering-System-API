from flask import Flask
from models import db
from api import api_bp
import stripe
import os



stripe_keys = {
        "secret_key": os.environ["STRIPE_SECRET_KEY"],
        "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
    }

stripe.api_key = stripe_keys["secret_key"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
    
if not os.path.exists("instance/database.db"):
    with app.app_context():
        db.create_all()


app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(debug=True)
from datetime import datetime
from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint
from my_app.product.models import PRODUCTS

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/sklep')
def home():
    return render_template('home.html', products=PRODUCTS, timestamp=datetime.now())

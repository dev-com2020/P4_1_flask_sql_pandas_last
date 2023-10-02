from flask import request, Blueprint, jsonify
from decimal import Decimal

catalog = Blueprint('catalog', __name__)

@catalog.route('/home')
def home():
    return 'Welcome to catalog 2023'

@catalog.route('/home/product/<key>')
def product(key):
    product = Product.query.filter_by(key=key).first_or_404()
    return 'Produkt - %s, %s' % (product.name, product.price)

@catalog.route('/home/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.key] = {
            'name': product.name,
            'price': str(product.price)
        }
    return jsonify(res)

@catalog.route('/home/product-create', method=['POST',])
def create_product():
    name = request.form.get('name')
    key = request.form.get('key')
    price = request.form.get('price')
    product = Product(
        name=name,
        key=key,
        price=Decimal(price)
    )
    db.session.add(product)
    db.session.commit()
    return 'Produkt dodany!'


from flask import request, Blueprint, jsonify, render_template
from decimal import Decimal

from my_app import db
from my_app.catalog.models import Product

catalog = Blueprint('catalog', __name__)


@catalog.route('/home')
def home():
    return 'Welcome to catalog 2023'


@catalog.route('/home/product/<key>')
def product(key):
    product = Product.query.filter_by(key=key).first_or_404()
    return 'Produkt - %s, %s' % (product.name, product.price)


@catalog.route('/home/products')
@catalog.route('/home/products/<int:page>')
def products(page=1):
    products = Product.query.paginate(page, 10).items
    res = {}
    for product in products:
        res[product.key] = {
            'name': product.name,
            'price': str(product.price),
            'category': product.category.name
        }
    return jsonify(res)


@catalog.route('/home/product-create', method=['POST', ])
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

@catalog.route('/category-create', methods=['POST',])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return render_template('category.html', category=category)

@catalog.route('/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)

@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('category.html', category=category)
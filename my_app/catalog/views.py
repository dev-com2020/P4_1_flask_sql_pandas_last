from flask import request, Blueprint, jsonify, render_template, flash
from decimal import Decimal

from my_app import db
from my_app.catalog.models import Product, Category

catalog = Blueprint('catalog', __name__)


@catalog.route('/home')
def home():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        products = Product.query.all()
        return jsonify({
            'count': len(products)
        })
    return render_template('home.html')


@catalog.route('/home/product/<id>')
def product(id):
    product = Product.query.first_or_404(id)
    return render_template('product.html', product=product)


@catalog.route('/home/products')
@catalog.route('/home/products/<int:page>')
def products(page=1):
    products = Product.query.paginate(page=page, per_page=10)
    return render_template('products.html', product=product)


@catalog.route('/home/product-create', method=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        key = request.form.get('key')
        price = request.form.get('price')
        categ_name = request.form.get('category')
        category = Category.query.filter_by(name=categ_name).first()
        if not category:
            category = Category(categ_name)
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        flash('Produkt %s został utworzony' % name, 'success')
    return render_template('product-create.html')


@catalog.route('/category-create', methods=['POST', ])
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

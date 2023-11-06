from functools import wraps

from flask import request, Blueprint, jsonify, render_template, flash, redirect, url_for
from decimal import Decimal

from sqlalchemy.orm import join

from my_app import db
from my_app.catalog.models import Product, Category

catalog = Blueprint('catalog', __name__)


def template_or_json(template=None):
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.headers.get("X-Requested-With") == "XMLHttpRequest" or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)

        return decorated_fn

    return decorated


@catalog.route('/home')
@template_or_json('/home.html')
def home():
    products = Product.query.all()
    return {'count': len(products)}


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
        return redirect(url_for('catalog.product', id=product.id))
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


@catalog.route('/product-search')
@catalog.route('/product-search/<int:page>')
def product_search(page=1):
    name = request.args.get('name')
    price = request.args.get('price')
    category = request.args.get('category')
    products = Product.query
    if name:
        products = products.filter(Product.name.like('%' + name + '%'))
    if price:
        products = products.filter(Product.price == price)
    if category:
        products = products.select_from(join(Product, Category)).filter(Category.name.like('%' + category + '%'))
    return render_template('products.html', products=products.paginate(page, 10))

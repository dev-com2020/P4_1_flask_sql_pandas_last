from functools import wraps

from flask import request, Blueprint, jsonify, render_template, flash, redirect, url_for
from decimal import Decimal

from sqlalchemy.orm import join

from my_app import db
from my_app.catalog.models import Product, Category, ProductForm, CategoryForm

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
    form = ProductForm(meta={'csrf': False})
    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices = categories
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        category = Category.query.get_or_404(form.category.data)
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        flash('Produkt %s został utworzony' % name, 'success')
        return redirect(url_for('catalog.product', id=product.id))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('product-create.html', form=form)


@catalog.route('/category-create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm(meta={'csrf': False})
    if form.validate_on_submit():
        name = form.name.data
        category = Category(name)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('catalog.category', id=category.id))
    if form.errors:
        flash(form.errors)
    return render_template('category.html', form=form)


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

import os.path
from _decimal import Decimal
from flask import Flask, request, jsonify

from my_app.catalog.models import db
from my_app.catalog.views import catalog
# from my_app.hello.views import hello
from markupsafe import Markup
from my_app.product.views import product_blueprint
import ccy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345@localhost/product'
app.secret_key = 'some_random_key'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg'}
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/my_app/static/uploads'
app.config['WTF_CSRF_SECRET_KEY'] = 'some_random_key'

# db = SQLAlchemy()

with app.app_context():
    db.create_all()

# app.register_blueprint(hello)
# app.register_blueprint(product_blueprint)
app.register_blueprint(catalog)


@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or 'USD'
    return f'{currency_code} {amount}'


class momentjs:
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return Markup(
            "<script>\ndocument.write(moment(\"%s\").%s);\n</script>" % (
                self.timestamp.strftime("%Y-%m-%dT%H:%M:%S"), format
            )
        )

    def format(self, fmt):
        return self.render("format(\"%s\")" % fmt)

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")

    def endOf(self, day):
        return self.render("endOf('day')")


app.jinja_env.globals['momentjs'] = momentjs

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     price = db.Column(db.Float, nullable=True)

# def __init__(self, name, price):
#     self.name = name
#     self.price = price
#
# def __repr__(self):
#     return f'<Product {self.id}>'


# @app.route('/home')
# def home():
#     return 'Welcome to catalog 2023'
#
#
# @app.route('/home/product/<id>')
# def product(id):
#     product = Product.query.filter_by(id).first_or_404()
#     return 'Produkt - %s, %s' % (product.name, product.price)
#
#
# @app.route('/home/products')
# def products():
#     products = Product.query.all()
#     res = {}
#     for product in products:
#         res[product.id] = {
#             'name': product.name,
#             'price': str(product.price)
#         }
#     return jsonify(res)
#
#
# @app.route('/home/product-create', methods=['POST', ])
# def create_product():
#     name = request.form.get('name')
#     price = request.form.get('price')
#     product = Product(
#         name=name,
#         price=Decimal(price)
#     )
#     db.session.add(product)
#     db.session.commit()
#     return 'Produkt dodany!'

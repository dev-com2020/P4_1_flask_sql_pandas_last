# PRODUCTS = {
#     'iphone': {
#         'name': 'Iphone 13',
#         'category': 'Phones',
#         'price': 1399
#     },
#     'samsung': {
#         'name': 'Galaxy 23',
#         'category': 'Phones',
#         'price': 1599
#     },
#     'nokia': {
#         'name': '3310',
#         'category': 'Phones',
#         'price': 399
#     }
# }
import datetime

from my_app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    key = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_id'))
    category = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'<Product {self.id}>'
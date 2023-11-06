import datetime
from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange

from my_app import db


# nosql!
# class Product(db.Document):
#     created_at = db.DateTimeField(
#         default=datetime.datetime.now, required=True
#     )
#     key = db.StringField(max_length=255, required=True)
#     name = db.StringField(max_length=255, required=True)
#     price = db.DecimalField()
#
#     def __repr__(self):
#         return '<Product %r>' % self.id


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    key = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_id'))
    category = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f'<Product {self.id}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category &d>' % self.id


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired(), NumberRange(min=Decimal(0.0))])
    category = SelectField('Category', coerce=int, validators=[InputRequired()])

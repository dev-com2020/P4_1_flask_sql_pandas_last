import datetime
from decimal import Decimal

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from markupsafe import Markup
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange, ValidationError
from wtforms.widgets import Select, html_params

from my_app import db

db = SQLAlchemy()

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
    image_path = db.Column(db.String(255))

    def __init__(self, name, price, category, image_path):
        self.name = name
        self.price = price
        self.category = category
        self.image_path = image_path

    def __repr__(self):
        return f'<Product {self.id}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category &d>' % self.id


class CategoryField(SelectField):
    def iter_choices(self):
        categories = [(c.id, c.name) for c in Category.query.all()]
        for value, label in categories:
            yield (value, label, self.coerce(value) == self.data)

    def pre_validate(self, form):
        for v, _ in [(c.id, c.name) for c in Category.query.all()]:
            if self.data == v:
                break
            else:
                raise ValueError(self.gettext('To nie jest prawidłowy wybór'))


class NameForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])


class ProductForm(NameForm):
    price = DecimalField('Price', validators=[InputRequired(), NumberRange(min=Decimal(0.0))])
    category = CategoryField('Category', coerce=int, validators=[InputRequired()])
    image = FileField('Product Image', validators=[FileRequired()])


def check_duplicate_category(case_sensitive=True):
    def _check_duplicate(form, field):
        if case_sensitive:
            res = Category.query.filter(
                Category.name.like('%' + field.data + '%')
            ).first()
        else:
            res = Category.query.filter(
                Category.name.ilike('%' + field.data + '%')
            ).first()
        if res:
            raise ValidationError(
                'Kategoria %s już istnieje' % field.data
            )
        return _check_duplicate


class CategoryForm(NameForm):
    name = StringField('Name', validators=[InputRequired(), check_duplicate_category()])


class CustomCategoryInput(Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = []
        for val, label, selected in field.iter_choices():
            html.append(
                '<input type="radio" %s> %s' % (
                    html_params(
                        name=field.name, value=val, checked=selected, **kwargs
                    ), label
                )
            )
        return Markup(' '.join(html))


class CategoryField(SelectField):
    widget = CustomCategoryInput()

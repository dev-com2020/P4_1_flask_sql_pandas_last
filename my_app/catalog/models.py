import datetime
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

    def __repr__(self):
        return f'<Product {self.id}>'

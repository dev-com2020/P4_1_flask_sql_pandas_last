from flask import Flask, request
from my_app.hello.views import hello
from markupsafe import Markup
from my_app.product.views import product_blueprint

app = Flask(__name__, static_folder='static')
app.register_blueprint(hello)
app.register_blueprint(product_blueprint)


# class momentjs:
#     def __init__(self, timestamp):
#         self.timestamp = timestamp
#
# def calendar(self):
#     return self.render("calendar()")
#
# app.jinja_env.globals['momentjs'] = momentjs
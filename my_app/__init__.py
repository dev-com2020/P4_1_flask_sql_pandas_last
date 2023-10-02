from flask import Flask, request
from my_app.hello.views import hello
from markupsafe import Markup
from my_app.product.views import product_blueprint

app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(product_blueprint)
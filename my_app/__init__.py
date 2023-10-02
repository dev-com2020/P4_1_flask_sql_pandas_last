from flask import Flask, request
from my_app.hello.views import hello
from markupsafe import Markup

app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(product_blueprint)
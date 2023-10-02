from flask import Flask, request
from my_app.hello.views import hello
from markupsafe import Markup
from my_app.product.views import product_blueprint
import ccy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345@localhost/dbname'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

app.register_blueprint(hello)
app.register_blueprint(product_blueprint)

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
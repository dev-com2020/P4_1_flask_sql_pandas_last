from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)


@hello.route('/')
def wizytowka():
    return '''
    <html>
    <head>
    <title>To jest tytuł strony...</title>
    </head>
    <body>
    <h2>Hello!</h2>
    <p>Witaj z aplikacji Flask!</p>
    </body>
    </html>
    '''



@hello.route('/hello')
def hello_world():
    return MESSAGES['default']


@hello.route('/great')
def hello_world2():
    return MESSAGES['great']


@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or f"{key} nie znaleziony!"


@hello.route('/add/<key>/<message>')
def add_or_update(key, message):
    MESSAGES[key] = message
    return f"{key} jest zaktualizowany!"

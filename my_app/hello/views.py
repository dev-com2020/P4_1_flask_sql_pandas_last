from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)


@hello.route('/')
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

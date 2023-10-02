from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)

@hello.route('/')
def hello_world():
    return MESSAGES['default']

@hello.route('/great')
def hello_world2():
    return MESSAGES['great']




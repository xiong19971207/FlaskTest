# @Author ：Bear
# @Date   ：2020/7/17 12:48

from flask import Blueprint

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/Test/')
def test():
    return 'Test'

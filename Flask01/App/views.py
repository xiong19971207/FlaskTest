# @Author ：Bear
# @Date   ：2020/6/27 20:04
from flask import Blueprint

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/index/')
def index():
    return 'Index'

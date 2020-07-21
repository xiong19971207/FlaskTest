# @Author ：Bear
# @Date   ：2020/7/21 9:20
from flask import Blueprint

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'

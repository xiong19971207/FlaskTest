# @Author ：Bear
# @Date   ：2020/7/20 9:38
from flask import Flask


from App.ext import init_ext
from App.models import db


def create_app():
    app = Flask(__name__)
    init_ext(app)
    return app

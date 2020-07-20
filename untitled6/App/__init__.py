# @Author ：Bear
# @Date   ：2020/7/19 11:23
from flask import Flask

from App.models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/SQL-ALCHEMY'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)
    return app

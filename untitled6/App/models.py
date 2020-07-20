# @Author ：Bear
# @Date   ：2020/7/19 17:22
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    color = db.Column(db.String(32))

    __tablename__ = 'animal1'
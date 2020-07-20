# @Author ：Bear
# @Date   ：2020/7/20 9:40
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    color = db.Column(db.String(32))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer)

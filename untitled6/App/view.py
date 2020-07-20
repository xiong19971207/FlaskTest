# @Author ：Bear
# @Date   ：2020/7/19 11:25
from flask import Blueprint, render_template

from App import db
from App.models import Animal

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/test/')
def test():
    return render_template('index.html')


@blue.route('/test2/')
def test2():
    return render_template('index2.html')


@blue.route('/create/')
def create():
    db.create_all()

    return '创建成功'


@blue.route('/drop/')
def drop():
    db.drop_all()

    return '删除成功'


@blue.route('/add/')
def add():
    a = Animal()
    a.name = 'hen'
    a.color = 'yellow'
    db.session.add(a)
    db.session.commit()

    return '添加成功'

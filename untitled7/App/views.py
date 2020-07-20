# @Author ：Bear
# @Date   ：2020/7/20 9:39
from flask import Blueprint

from App.models import Student, db

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/addstudent/')
def addstudent():
    s = Student()
    s.name = 'zs'

    db.session.add(s)
    db.session.commit()

    return '添加成功'


@blue.route('/updatestudent/')
def updatestudent():
    s = Student.query.first()
    s.name = 'ls'

    db.session.add(s)
    db.session.commit()

    return '修改成功'


@blue.route('/searchstudent/')
def searchstudent():
    s = Student.query.filter_by(id=1)
    print(type(s))

    return '查询成功'


@blue.route('/order/')
def order():
    # s_list = Student.query.order_by('age')
    # for s in s_list:
    #     print(s.name, s.age)

    s_list = Student.query.order_by(db.desc('age'))
    for s in s_list:
        print(s.name, s.age)
    return '查询成功'

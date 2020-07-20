# @Author ：Bear
# @Date   ：2020/7/18 14:57
from flask import Blueprint, render_template, request, redirect, url_for, session

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/login/')
def login():
    return render_template('login.html')


@blue.route('/set_session/', methods=['post'])
def set_session():
    name = request.form.get('name')
    response = redirect(url_for('blue.welcome'))
    session['name'] = name
    return response


@blue.route('/welcome/')
def welcome():
    name = session.get('name', '游客')
    return render_template('welcome.html', name=name)


@blue.route('/loginout/')
def loginout():
    response = redirect(url_for('blue.welcome'))
    response.delete_cookie('session')
    return response

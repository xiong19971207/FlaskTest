# @Author ：Bear
# @Date   ：2020/7/9 20:40


from flask import Blueprint, request, redirect, abort, render_template, url_for

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    print(request.cookies)

    return 'Hello World!'


@blue.route('/test/')
def test():
    return 'TEST'


@blue.route('/test1/')
def test1():
    return 'Welcome to 东北'


@blue.route('/test2/')
def test2():
    r = redirect('/test1/')
    print(type(r))
    return r


@blue.route('/testAbort/')
def testAbort():
    abort(500)
    return 'testAbort'


@blue.route('/login/')
def login():
    return render_template('login.html')


@blue.route('/make_cookie/', methods=['post'])
def make_cookie():
    name = request.form.get('name')
    response = redirect(url_for('blue.welcome'))
    response.set_cookie('name', name)
    return response


@blue.route('/welcome/')
def welcome():
    name = request.cookies.get('name', '游客')
    return render_template('welcome.html', name=name)


@blue.route('/loginout/')
def loginout():
    response = redirect(url_for('blue.welcome'))
    response.delete_cookie('name')
    return response

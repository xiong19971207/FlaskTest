# @Author ：Bear
# @Date   ：2020/7/18 14:56


from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'xxr'
    return app

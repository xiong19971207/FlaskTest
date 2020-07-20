# @Author ：Bear
# @Date   ：2020/6/27 16:32


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '左边画一条龙'


if __name__ == '__main__':
    app.run()

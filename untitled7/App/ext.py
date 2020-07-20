# @Author ：Bear
# @Date   ：2020/7/20 9:57
from flask_migrate import Migrate
from flask_session import Session

from App.models import db



def init_ext(app):

    app.config['SECRET_KEY'] = 'xiong'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'python'
    Session(app=app)

    # sqlalchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/SQL-ALCHEMY'
    db.init_app(app=app)

    # flask-migrate
    migrate = Migrate()
    migrate.init_app(db=db,app=app)
from flask_script import Manager

from app import create_app
from app.view import blue

app = create_app()

manager = Manager(app=app)

app.register_blueprint(blueprint=blue)

if __name__ == '__main__':
    manager.run()

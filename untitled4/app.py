from App import create_app
from App.view import blue

app = create_app()

app.register_blueprint(blueprint=blue)

if __name__ == '__main__':
    app.run()

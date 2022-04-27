# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример
from flask import Flask
from flask_restx import Api

from application.config import Config
from application.setup_db import db
from application.views.movie import movies_ns
from application.views.director import directors_ns
from application.views.genre import genres_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app: Flask):
    db.init_app(app)
    api = Api(app, prefix='/api', doc='/docs')
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    create_data(app, db)


# функция
def create_data(app, db):
    with app.app_context():
        db.create_all()

        # создать несколько сущностей чтобы добавить их в БД

        # with db.session.begin():
        #     db.session.add_all()
            # (здесь список созданных объектов)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001)

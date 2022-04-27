from flask import Flask
from flask_restx import Api, cors
from flask_cors import CORS
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    cors.init_app(app)
    db.init_app(app)

    register_extensions(app)
    return app


def register_extensions(app):

    db.init_app(app)
    api = Api(app)
    api.init_app(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

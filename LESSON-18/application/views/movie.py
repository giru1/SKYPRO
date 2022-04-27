# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from application.container import movies_services
from application.dao.model.movie import MovieSchema

movies_ns = Namespace('movies')
movie_schema = MovieSchema()


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id: int):
        return movies_services.get_one(id)

    def put(self, id: int):
        try:
            return movies_services.update(id, request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

    def delete(self, id: int):
        movies_services.delete(id)

        return {}, 204



@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data = request.args

        if 'director_id' in data:
            return movies_services.get_director_id(data['director_id'])
        if 'genre_id' in data:
            return movies_services.get_genre_id(data['genre_id'])

        return movies_services.get_all()
        # return movie_schema.dump(movies_dao.get_all())

    def post(self):
        return movies_services.create(request.json)

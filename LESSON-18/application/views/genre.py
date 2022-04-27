# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.genre import GenreSchema
from application.container import genre_services

genres_ns = Namespace('genres')
genre_schema = GenreSchema()


@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genre_services.get_all()

    def post(self):
        return genre_services.create(request.json)


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id: int):
        return genre_services.get_one(id)

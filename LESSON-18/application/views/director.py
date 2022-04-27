# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.director import DirectorSchema



from application.container import director_services

directors_ns = Namespace('directors')
director_schema = DirectorSchema()


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return director_services.get_all()

    def post(self):
        return director_services.create(request.json)


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id: int):
        return director_services.get_one(id)

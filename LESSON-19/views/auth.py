from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        print(auth_service.login(request.json))
        return auth_service.login(request.json)

    def put(self):
        return auth_service.get_new_token(request.json['refresh_token'])

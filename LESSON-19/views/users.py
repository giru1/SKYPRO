from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service
from utils import auth_required, admin_access_required

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        data = request.args
        # print(data)
        all_movies = user_service.get_all()
        res = UserSchema(many=True).dump(all_movies)
        # print(res)
        return res, 200

    @admin_access_required
    def post(self):
        user_service.register(request.json)
        return {}, 201


@user_ns.route('/<int:bid>')
class UserView(Resource):
    @auth_required
    def get(self, bid):
        b = user_service.get_one(bid)
        sm_d = UserSchema().dump(b)
        return sm_d, 200

    @admin_access_required
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        user_service.update(req_json)
        return "", 204

    @admin_access_required
    def delete(self, bid):
        user_service.delete(bid)
        return "", 204


# @user_ns.route('/<username>')
# class UserViewUsername(Resource):
#     @auth_required
#     def get(self, username):
#         # print(user_service.get_by_username(username))
#         return user_service.get_by_username(username)

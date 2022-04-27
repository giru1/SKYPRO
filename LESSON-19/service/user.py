import base64
import hashlib

import constants
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register(self, data: dict) -> dict:
        data['password'] = get_hashed_pass(data['password'])
        self.dao.create(data)
        return data

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)


def get_hashed_pass(password: str) -> str:
    return base64.b64encode(hashlib.pbkdf2_hmac(
        hash_name=constants.HASH_NAME,
        salt=constants.HASH_SALT.encode('utf-8'),
        iterations=constants.HASH_GEN_ITERATIONS,
        password=password.encode('utf-8')
    )).decode('utf-8', "ignore")

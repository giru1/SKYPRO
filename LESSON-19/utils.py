import base64
import hashlib
from datetime import timedelta, datetime
from typing import Dict

import jwt
from flask import request
from flask_restx import abort
from setup_db import db
import constants
from dao.user import UserDAO
from service.user import UserService
user_dao = UserDAO(session=db.session)
user_service = UserService(dao=user_dao)


def get_hashed_pass(password: str) -> str:
    return base64.b64encode(hashlib.pbkdf2_hmac(
        hash_name=constants.HASH_NAME,
        salt=constants.HASH_SALT.encode('utf-8'),
        iterations=constants.HASH_GEN_ITERATIONS,
        password=password.encode('utf-8')
    )).decode('utf-8', "ignore")


def genereta_tokens(data: dict) -> Dict[str, str]:
    data['exp'] = datetime.utcnow() + timedelta(minutes=30)
    data['refresh_token'] = False

    access_token: str = jwt.encode(
        payload=data,
        key=constants.SECRET_HERE,
        algorithm=constants.JWT_ALGORITHM,
    )

    data['exp'] = datetime.utcnow() + timedelta(days=30)
    data['refresh_token'] = True

    refresh_token: str = jwt.encode(
        payload=data,
        key=constants.SECRET_HERE,
        algorithm=constants.JWT_ALGORITHM,
    )

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }


def get_token_headera(headers: dict):
    if 'Authorization' not in headers:
        abort(401)

    return headers['Authorization'].split(' ')[-1]


def decode_token(token: str, refresh_token: bool = False):
    decode_token = {}
    try:
        decode_token = jwt.decode(
            jwt=token,
            key=constants.SECRET_HERE,
            algorithms=[constants.JWT_ALGORITHM],
        )
    except jwt.PyJWTError as e:
        abort(401, message='no valid token')

    if decode_token['refresh_token'] != refresh_token:
        abort(400, message='wrong token type')

    return decode_token


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = get_token_headera(request.headers)
        decoded_token = decode_token(token)
        print(decoded_token['username'])
        print(decoded_token)
        print(type(decoded_token))
        if not user_service.get_by_username(decoded_token.get('username')):
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_access_required(func):
    def wrapper(*args, **kwargs):
        token = get_token_headera(request.headers)

        decoded_token = decode_token(token)
        if decoded_token['role'] != 'admin':
            abort(403)
        return func(*args, **kwargs)

    return wrapper

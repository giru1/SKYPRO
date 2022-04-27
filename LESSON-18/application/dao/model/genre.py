# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)
from marshmallow import Schema, fields
from application.dao.model.base import BaseModal
from application.setup_db import db


# from setup_db import db


class Genre(BaseModal):
    __tablename__ = 'genre'
    name = db.Column(db.String(100), nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

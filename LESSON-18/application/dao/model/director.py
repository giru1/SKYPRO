from marshmallow import Schema, fields
from application.dao.model.base import BaseModal
from application.setup_db import db


class Director(BaseModal):
    __tablename__ = 'director'
    name = db.Column(db.String(100), nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

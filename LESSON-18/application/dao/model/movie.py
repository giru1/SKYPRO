from marshmallow import Schema, fields, validates, ValidationError, validates_schema

from application.setup_db import db
from application.dao.model.base import BaseModal


class Movie(BaseModal):
    __tablename__ = 'movie'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))

    genre = db.relationship("Genre")
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()

    @validates_schema(pass_many=True)
    def root_validate(self, data, **kwargs):
        if data['title'] == 'test':
            raise ValidationError('Title cannot ne test')
        return data

    # @validates('year')
    # def validate_year(self, value: int):
    #     if value > 2022:
    #         raise ValidationError('Year error!')
    #     return value

from typing import Dict, Any

from marshmallow import ValidationError

from application.dao.model.movie import Movie
from lib.dao import BaseDAO


class MoviesDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, id: int):
        return self.session.query(Movie).filter(Movie.id == id).first()

    def create(self, data: Dict[str, Any]):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, id: int, data: Dict[str, Any]):
        result = self.session.query(Movie).filter(Movie.id == id).update(data)
        if result != 1:
            self.session.rollback()
            raise ValidationError(f'Movie with id {id} not found')

        self.session.commit()

    def delete(self, id: int):
        self.session.query(Movie).filter(Movie.id == id).delete()
        self.session.commit()

    def get_director_id(self, director_id: int):
        self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_genre_id(self, genre_id: int):
        self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

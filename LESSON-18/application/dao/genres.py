from typing import Dict, Any

from marshmallow import ValidationError

from lib.dao import BaseDAO
from application.dao.model.genre import Genre


class GenresDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, id: int):
        return self.session.query(Genre).filter(Genre.id == id).first()

    def update(self, id: int, data: Dict[str, Any]):
        result = self.session.query(Genre).filter(Genre.id == id).update(data)
        if result != 1:
            self.session.rollback()
            raise ValidationError(f'Movie with id {id} not found')

        self.session.commit()

    def delete(self, id: int):
        self.session.query(Genre).filter(Genre.id == id).delete()
        self.session.commit()
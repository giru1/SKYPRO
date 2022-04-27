from typing import Dict, Any

from marshmallow import ValidationError

from lib.dao import BaseDAO
from application.dao.model.director import Director


class DirectorsDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, id: int):
        return self.session.query(Director).filter(Director.id == id).first()

    def update(self, id: int, data: Dict[str, Any]):
        result = self.session.query(Director).filter(Director.id == id).update(data)
        if result != 1:
            self.session.rollback()
            raise ValidationError(f'Movie with id {id} not found')

        self.session.commit()

    def delete(self, id: int):
        self.session.query(Director).filter(Director.id == id).delete()
        self.session.commit()
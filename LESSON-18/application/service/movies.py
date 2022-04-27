from lib.service import BaseService


class MoviesService(BaseService):

    def get_director_id(self, director_id: int):
        return self.schema.dump(self.dao.get_director_id(director_id), many=True)

    def get_genre_id(self, genre_id: int):
        return self.schema.dump(self.dao.get_genre_id(genre_id), many=True)

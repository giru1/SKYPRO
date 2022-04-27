from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao_fixture():
    dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title='Йеллоустоун',
        description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        trailer='www.youtube.com/',
        year=2018,
        rating=8.6,
        genre_id=17,
        director_id=1
    )

    movie2 = Movie(
        id=1,
        title='Йеллоустоун',
        description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        trailer='www.youtube.com/',
        year=2018,
        rating=8.6,
        genre_id=17,
        director_id=1
    )

    dao.get_one = MagicMock(return_value={
        'id': 1,
        'title': 'Йеллоустоун',
        'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        'trailer': 'www.youtube.com/',
        'year': 2018,
        'rating': 8.6,
        'genre_id': 17,
        'director_id': 1
    })

    dao.get_all = MagicMock(return_value=[
            {
                'id': 1,
                'title': 'Йеллоустоун',
                'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
                'trailer': 'www.youtube.com/',
                'year': 2018,
                'rating': 8.6,
                'genre_id': 17,
                'director_id': 1
            },
            {
                'id': 1,
                'title': 'Йеллоустоун',
                'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
                'trailer': 'www.youtube.com/',
                'year': 2018,
                'rating': 8.6,
                'genre_id': 17,
                'director_id': 1
            },
        ])

    dao.create = MagicMock(return_value={
        'id': 1,
        'title': 'Йеллоустоун 2',
        'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        'trailer': 'www.youtube.com/',
        'year': 2018,
        'rating': 8.6,
        'genre_id': 17,
        'director_id': 1
    })
    dao.update = MagicMock(return_value={
        'id': 1,
        'title': 'new Йеллоустоун',
        'description': '1Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        'trailer': 'www.youtube.com/1',
        'year': 2022,
        'rating': 10,
        'genre_id': 17,
        'director_id': 1
    })
    dao.delete = MagicMock(return_value={})

    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        all_movies = self.movie_service.get_all()

        assert len(all_movies) > 0
        assert type(all_movies) == list

    def test_create(self):
        movie_new = self.movie_service.create(1)

        assert movie_new is not None
        assert type(movie_new) == dict

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        updated_movie = self.movie_service.update(1)

        assert updated_movie['title'] == 'new Йеллоустоун'
        assert type(updated_movie) == dict

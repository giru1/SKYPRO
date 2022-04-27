from application.dao.model.director import DirectorSchema
from application.dao.model.genre import GenreSchema
from application.dao.model.movie import MovieSchema

from application.dao.directors import DirectorsDAO
from application.dao.genres import GenresDAO
from application.dao.movies import MoviesDAO

from lib.service import BaseService

from application.service.movies import MoviesService

from application.setup_db import db

movie_schema = MovieSchema()
movies_dao = MoviesDAO(db.session)
movies_services = MoviesService(movies_dao, movie_schema)

director_schema = DirectorSchema()
director_dao = DirectorsDAO(db.session)
director_services = BaseService(director_dao, director_schema)

genre_schema = GenreSchema()
genre_dao = GenresDAO(db.session)
genre_services = BaseService(genre_dao, genre_schema)
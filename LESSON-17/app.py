# app.py

from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
api = Api(app)
movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = Movie.query.get(id)

        return movies_schema.dump(movie), 200

    def put(self, id):
        req_json = request.json
        db.session.query(Movie).filter(Movie.id == id).update(req_json)
        db.session.commit()
        return None, 204

    def delete(self, id):
        db.session.query(Movie).filter(Movie.id == id).delete()
        db.session.commit()
        return 202


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query.all()
        data = request.args

        director_id = data.get('director_id')
        genre_id = data.get('genre_id')

        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)

        if genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)

        if genre_id and director_id:
            movies = Movie.query.filter(Movie.director_id == director_id, Movie.genre_id == genre_id)

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@directors_ns.route('/<int:d_id>')
class DirectorView(Resource):
    def get(self, d_id):
        director = Director.query.get(d_id)
        return director_schema.dump(director), 200

    def put(self, d_id):
        req_json = request.json
        db.session.query(Director).filter(Director.id == d_id).update(req_json)
        db.session.commit()
        return None, 204

    def delete(self, d_id):
        db.session.query(Director).filter(Director.id == d_id).delete()
        db.session.commit()
        return 202


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        return directors_schema.dump(directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genres_ns.route('/<int:g_id>')
class GenreView(Resource):
    def get(self, g_id):
        genre = Genre.query.get(g_id)
        return genre_schema.dump(genre), 200

    def put(self, g_id):
        req_json = request.json
        db.session.query(Genre).filter(Genre.id == g_id).update(req_json)
        db.session.commit()
        return None, 204

    def delete(self, g_id):
        db.session.query(Genre).filter(Genre.id == g_id).delete()
        db.session.commit()
        return 202


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        return genres_schema.dump(genres), 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


if __name__ == '__main__':
    app.run(debug=True)

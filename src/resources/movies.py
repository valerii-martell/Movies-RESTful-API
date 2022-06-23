import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload, selectinload

from src import db
from src.database.models import Movie
from src.resources.auth import token_required
from src.schemas.movies import MovieSchema


class MoviesListApi(Resource):
    movie_schema = MovieSchema()

    #@token_required
    def get(self, uuid=None):
        if not uuid:
            movies = db.session.query(Movie).options(
                joinedload(Movie.actors)
                # selectinload(Movie.actors)
            ).all()
            return self.movie_schema.dump(movies, many=True), 200
        movie = db.session.query(Movie).filter_by(uuid=uuid).first()
        if not movie:
            return '', 404
        return self.movie_schema.dump(movie), 200

    def post(self):
        try:
            movie = self.movie_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': "str(e)"}, 400
        db.session.add(movie)
        db.session.commit()
        return self.movie_schema.dump(movie), 201

    def put(self, uuid):
        movie = db.session.query(Movie).filter_by(uuid=uuid).first()
        if not movie:
            return "", 404
        try:
            movie = self.movie_schema.load(request.json, instance=movie, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(movie)
        db.session.commit()
        return self.film_schema.dump(movie), 200

    def patch(self, uuid):
        movie = db.session.query(Movie).filter_by(uuid=uuid).first()
        if not movie:
            return "", 404
        movie_json = request.json
        title = movie_json.get('title')
        release_date = datetime.datetime.strptime(movie_json.get('release_date'), '%B %d, %Y') if movie_json.get(
            'release_date') else None
        distributed_by = movie_json.get('distributed_by'),
        rating = movie_json.get('rating'),
        length = movie_json.get('length'),
        description = movie_json.get('description')

        if title:
            movie.title = title
        elif release_date:
            movie.release_date = release_date
        elif distributed_by:
            movie.distributed_by = distributed_by
        elif rating:
            movie.rating = rating
        elif length:
            movie.length = length
        elif description:
            movie.description = description

        db.session.add(movie)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        movie = db.session.query(Movie).filter_by(uuid=uuid).first()
        if not movie:
            return "", 404
        db.session.delete(movie)
        db.session.commit()
        return '', 204

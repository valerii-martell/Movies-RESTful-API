import datetime

from flask import request
from flask_restful import Resource
from src import api, db
from src.models import Movie


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}, 200


class MoviesListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            movies = db.session.query(Movie).all()
            return [movie.to_dict() for movie in movies], 200
        movie = db.session.query(Movie).filter_by(uuid=uuid).first()
        if not movie:
            return '', 404
        return movie.to_dict(), 200

    def post(self):
        movie_json = request.json
        if not movie_json:
            return {'message': 'Wrong data'}, 400
        try:
            movie = Movie(
                title=movie_json['title'],
                release_date=datetime.datetime.strptime(movie_json['release_date'], '%B %d, %Y'),
                distributed_by=movie_json['distributed_by'],
                rating=movie_json.get('rating'),
                length=movie_json.get('length'),
                description=movie_json.get('description')
            )
            db.session.add(movie)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully', 'uuid': movie.uuid}, 201

    def put(self, uuid):
        movie_json = request.json
        if not movie_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Movie).filter_by(uuid=uuid).update(
                dict(
                    title=movie_json['title'],
                    release_date=datetime.datetime.strptime(movie_json['release_date'], '%B %d, %Y'),
                    distributed_by=movie_json['distributed_by'],
                    rating=movie_json.get('rating'),
                    length=movie_json.get('length'),
                    description=movie_json.get('description')
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 200

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


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(MoviesListApi, '/movies', '/movies/<uuid>', strict_slashes=False)

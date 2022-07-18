from src.database.models import Movie


class MovieService:
    @staticmethod
    def fecth_all_movies(session):
        return session.query(Movie)

    @classmethod
    def fetch_movie_by_uuid(cls, session, uuid):
        return cls.fecth_all_movies(session).filter_by(uuid=uuid).first()

    @staticmethod
    def bulk_create_movies(session, movies):
        movies_to_create = [
            Movie(**movie)
            for movie in movies
        ]
        session.bulk_save_objects(movies_to_create)
        session.commit()
        return len(movies_to_create)

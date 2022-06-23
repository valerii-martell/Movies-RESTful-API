from src.database.models import Movie


class MovieService:
    @staticmethod
    def fecth_all_movies(session):
        return session.query(Movie)

    @classmethod
    def fetch_movie_by_uuid(cls, session, uuid):
        return cls.fecth_all_movies(session).filter_by(uuid=uuid).first()



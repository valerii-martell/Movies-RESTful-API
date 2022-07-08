from src.database.models import Actor


class ActorService:
    @staticmethod
    def fecth_all_actors(session):
        return session.query(Actor)

    @classmethod
    def fetch_actor_by_uuid(cls, session, uuid):
        return cls.fecth_all_actors(session).filter_by(uuid=uuid).first()

    @staticmethod
    def bulk_create_actors(session, actors):
        actors_to_create = [
            Actor(**actor)
            for actor in actors
        ]
        session.bulk_save_objects(actors_to_create)
        session.commit()
        return len(actors_to_create)



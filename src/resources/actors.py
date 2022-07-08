from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Actor
from src.resources.auth import token_required, admin_token_required
from src.schemas.actors import ActorSchema
from src.services.actor_servise import ActorService


class ActorsListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, uuid=None):
        if not uuid:
            movies = ActorService.fecth_all_actors(db.session).all()
            return self.actor_schema.dump(movies, many=True), 200
        actor = ActorService.fetch_actor_by_uuid(db.session, uuid)
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

    @token_required
    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, uuid):
        pass

    @admin_token_required
    def delete(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return "", 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204

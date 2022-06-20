from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models import Movie, Actor


class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True


class MovieSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        exclude = ['id']
        load_instance = True

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import Movie


class MovieSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        exclude = ['id']
        load_instance = True

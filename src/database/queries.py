"""
SELECT QUERIES
"""
from sqlalchemy import and_

from src import db
from src.database import models

# movies = db.session.query(models.Movie).order_by(models.Movie.rating.desc()).all()
# print(movies)
# harry_potter_and_ch_s = db.session.query(models.Movie).filter(
#     models.Movie.title == 'Harry Potter and Chamber of Secrets'
# ).first()
# print(harry_potter_and_ch_s)
# harry_potter_priz_az = db.session.query(models.Movie).filter_by(
#     title='Harry Potter and the Prizoner of Azkaban'
# ).first()
# and_statement_harry_potter = db.session.query(models.Movie).filter(
#     and_(
#         models.Movie.title != 'Harry Potter and Chamber of Secrets',
#         models.Movie.rating >= 7.5
#     )
# ).all()
# deathy_hallows = db.session.query(models.Movie).filter(
#     models.Movie.title.ilike('%deathly hallows%')
# ).all()
# harry_potter_sorted_by_length = db.session.query(models.Movie).filter(
#     ~models.Movie.length.in_([146, 161]))[:3]
# print(harry_potter_sorted_by_length)
# """
# QUERYING WITH JOINS
# """
# movies_with_actors = db.session.query(models.Movie).join(models.Movie.actors).all()
# print(movies_with_actors)


# actor = db.session.query(models.Actor).first()
# print(actor.movies)

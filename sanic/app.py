import datetime

from aiopg.sa import create_engine
from sanic import Sanic, response
from sanic.views import HTTPMethodView
from sqlalchemy import select

import config
from src.database.models import Movie

app = Sanic(__name__)


class AsyncMovieService:
    @classmethod
    async def fetch_all_movies(cls):
        async with create_engine(config.Config.SQLALCHEMY_DATABASE_URI) as engine:
            async with engine.acquire() as conn:
                query = select([Movie])
                result = await conn.execute(query)
                movies = []
                async for row in result:
                    movies.append(dict(row))
        return movies


class MovieListApi(HTTPMethodView):
    async def get(self, request):
        movies = await AsyncMovieService.fetch_all_movies()
        for f in movies:
            f['release_date'] = datetime.datetime.strftime(f['release_date'], '%Y-%m-%d')
        return response.json(movies)


class Smoke(HTTPMethodView):
    async def get(self, request):
        return response.json(
            {'hello': 'world'}
        )


app.add_route(Smoke.as_view(), '/smoke')
app.add_route(MovieListApi.as_view(), '/movies')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, workers=4)
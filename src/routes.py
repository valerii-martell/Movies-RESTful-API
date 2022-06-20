from src import api, db
from src.resources.actors import ActorsListApi
from src.resources.movies import MoviesListApi
from src.resources.smoke import Smoke

api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(MoviesListApi, '/movies', '/movies/<uuid>', strict_slashes=False)
api.add_resource(ActorsListApi, '/actors', '/actors/<uuid>', strict_slashes=False)

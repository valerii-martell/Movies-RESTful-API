from src import api
from src.resources.actors import ActorsListApi
from src.resources.aggregations import AggregationsApi
from src.resources.auth import AuthRegister, AuthLogin
from src.resources.index import Index
from src.resources.movies import MoviesListApi
from src.resources.populate_db import PopulateDB, PopulateDBThreads, PopulateDBProcesses
from src.resources.smoke import Smoke

api.add_resource(Index, '/', strict_slashes=False)
api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(MoviesListApi, '/movies', '/movies/<uuid>', strict_slashes=False)
api.add_resource(ActorsListApi, '/actors', '/actors/<uuid>', strict_slashes=False)
api.add_resource(AggregationsApi, '/aggregations', strict_slashes=False)
api.add_resource(AuthRegister, '/register', strict_slashes=False)
api.add_resource(AuthLogin, '/login', strict_slashes=False)
api.add_resource(PopulateDB, '/populate/sequentially', strict_slashes=False)
api.add_resource(PopulateDBThreads, '/populate/threads', strict_slashes=False)
api.add_resource(PopulateDBProcesses, '/populate/processes', strict_slashes=False)

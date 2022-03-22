from .movie import MoviesApi, MovieApi
from .auth import SignUpApi, LoginApi


def initialize_routes(api):

    # Movies
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<movie_id>')

    # Users
    api.add_resource(SignUpApi, '/api/auth/singup')
    api.add_resource(LoginApi, '/api/auth/login')

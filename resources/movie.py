from flask import Response, request
from database.db import mongo
from flask_pymongo import ObjectId
from bson.json_util import dumps
from flask_restful import Resource
from typing import Union


class MoviesApi(Resource):

    def get(self: object) -> Union[dict[str, str], Response]:
        movies: list = list(mongo.db.movies.find())
        if not movies:
            return {'message': 'No movies found.'}
        return Response(dumps(movies), mimetype='application/json', status=200)

    def post(self: object):
        new_movie = request.get_json()
        new_movie_id = mongo.db.movies.insert_one(new_movie)
        return {'_id': str(new_movie_id.inserted_id)}, 200


class MovieApi(Resource):

    def put(self: object):
        edited_movie = request.get_json()
        mongo.db.movies.update_one({'_id': ObjectId(id)}, {'$set': edited_movie})
        return {'message': 'Movie has been updated.'}, 200

    def delete(self: object, movie_id):
        mongo.db.movies.delete_one({"_id": ObjectId(movie_id)})
        return {'message': 'Movie has been deleted.'}, 200

    def get(self: object, movie_id) -> Union[dict[str, str], Response]:
        movie = mongo.db.movies.find_one_or_404({'_id': ObjectId(movie_id)})
        return Response(dumps(movie), mimetype='application/json', status=200)

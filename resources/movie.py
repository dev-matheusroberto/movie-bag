from flask import Response, request
from database.db import mongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class MoviesApi(Resource):

    @jwt_required
    def get(self: object):
        movies: list = list(mongo.db.movies.find())
        if not movies:
            return {'message': 'No movies found.'}
        return Response(dumps(movies), mimetype='application/json', status=200)

    @jwt_required
    def post(self: object):
        new_movie = request.get_json()
        new_movie_id = mongo.db.movies.insert_one(new_movie)
        return {'_id': str(new_movie_id.inserted_id)}, 200


class MovieApi(Resource):

    @jwt_required
    def put(self: object):
        edited_movie = request.get_json()
        mongo.db.movies.update_one({'_id': ObjectId(id)}, {'$set': edited_movie})
        return {'message': 'Movie has been updated.'}, 200

    @jwt_required
    def delete(self: object, movie_id):
        mongo.db.movies.delete_one({"_id": ObjectId(movie_id)})
        return {'message': 'Movie has been deleted.'}, 200

    @jwt_required
    def get(self: object, movie_id):
        movie = mongo.db.movies.find_one_or_404({'_id': ObjectId(movie_id)})
        return Response(dumps(movie), mimetype='application/json', status=200)

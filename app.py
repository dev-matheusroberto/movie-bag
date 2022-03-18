from flask import Flask, request, Response
from database.db import mongo
from flask_pymongo import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB Config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/movie-bag'
mongo.init_app(app)


@app.route('/movies', methods=['GET'])
def get_movies():
    movies: list = list(mongo.db.movies.find())
    if not movies:
        return {'message': 'No movies found.'}
    return Response(dumps(movies), mimetype='application/json', status=200)


@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    movie = mongo.db.movies.find_one_or_404({'_id': ObjectId(id)})
    return Response(dumps(movie), mimetype='application/json', status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = request.get_json()
    mongo.db.movies.insert_one(new_movie)
    return {'id': str(id)}, 200


@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    edited_movie = request.get_json()
    mongo.db.movies.update_one({'_id': ObjectId(id)}, {'$set': edited_movie})
    return {'message': 'Movie has been updated.'}, 200


@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    mongo.db.movies.delete_one({"_id": ObjectId(id)})
    return '', 200


app.run(debug=True)

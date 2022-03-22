from flask import Response, request
from flask_jwt_extended import create_access_token
from bson.objectid import ObjectId
from database.db import mongo
from bson.json_util import dumps
from flask_restful import Resource
from resources.security import hash_password, check_password_hash
from datetime import datetime, timedelta


class SignUpApi(Resource):
    
    def post(self: object):
        new_user = {
            'email': request.json.get('email'),
            'password': hash_password(request.json.get('password'))
        }
        new_user_id = mongo.db.users.insert_one(new_user).inserted_id
        return {'_id': new_user_id}, 200


class LoginApi(Resource):

    def post(self: object):
        user = {'email': request.json.get('email')}
        a_user = mongo.db.users.find_one(user)

        authorized = check_password_hash(a_user['password'], request.json.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        access_token = create_access_token(identity=str(user), expires_delta=timedelta(hours=24))
        expires = datetime.now() + timedelta(hours=24)

        response = {
            'message': 'Login successful!',
            'token': access_token,
            'expires': expires.strftime('%Y-%m-%d %H:%M:%S')
        }

        return response, 200

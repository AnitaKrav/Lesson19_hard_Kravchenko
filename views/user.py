from flask import request
from flask_restx import Namespace, Resource

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')

@user_ns.route('/')
class UsersView(Resource):

    def get(self):
        users = user_service.get_all()
        res = UserSchema(many=True).dump(users)
        return res, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201,  {"location": f"/users/{user.id}"}

@user_ns.route('<int:uid>')
class UserView(Resource):

    def get(self, uid):
        user = user_service.get_one(uid)

        user_schema = UserSchema().dump(user)

        return user_schema, 200

    def put(self, uid):
        req_json = request.json

        if 'id' not in req_json:
            req_json['id'] = uid

        user_service.upadate(req_json)

    def delete(self, uid):
        user_service.delete(uid)

        return "", 204


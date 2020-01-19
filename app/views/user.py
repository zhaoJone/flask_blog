from flask import request

from models.user import User
from schemas.user import UserSchema
from helpers.view import BaseView
from helpers.response import response
from helpers.exceptions import ServerError


class UserView(BaseView):
    model = User
    schema = UserSchema


class UserApi(UserView):

    def get(self):
        users = self.model.query.all()
        data = self.schema().dump(users, many=True)

        return response(data)

    def post(self):
        body = request.get_json()
        user = self.schema().load(body)
        data = self.schema().dump(user)
        return response(data)


class UserItemApi(UserView):

    def get(self, user_id):
        user = self.model.query.filter(self.model.id == user_id).first()
        if user is None:
            data = {}
        else:
            data = self.schema().dump(user)
        return response(data)

    def put(self, user_id):
        raise NotImplementedError

    def delete(self, user_id):
        raise NotImplementedError


def index():
    raise ServerError
    return response({'data': 'hello world!!!!'})

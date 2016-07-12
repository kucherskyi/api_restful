#! env/bin/python

from flask import jsonify
from flask_restful import reqparse, abort, Resource, fields, marshal_with
import hashlib

from app import db
from models import Base, User


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('password')
parser.add_argument('info')


class UsersList(Resource):
    def get(self):
        user = User.query.all()
        all_users = []
        for row in user:
            all_users.append({'name': row.name, 'id': row.id})
        return jsonify(all_users)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        password = hashlib.md5(args['password']).hexdigest()
        info = args['info']
        if User.query.filter_by(name=name).first() is not None:
            abort(400, error_message='user exists')
        user = User(name=name, info=info, password=password)
        db.session.add(user)
        db.session.commit()
        return args['name'], 201


class Users(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(400, error_message='No user with id={}'.format(user_id))
        return jsonify({'name': user.name, 'info': user.info})

    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return 'deleted', 204

    def put(self, user_id):
        args = parser.parse_args()
        user = User.query.get(user_id)
        user.info = args['info']
        db.session.add(user)
        db.session.commit()
        return jsonify({'name': user.info})

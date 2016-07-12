#! env/bin/python

from flask import jsonify
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from models import Base, User
from app import db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('password')
parser.add_argument('info')

class Users(Resource):
    def get(self):
        user = User.query.all()
        al = []
        for row in user:
            al.append({'User': row.name})
        return jsonify(al), 200


    def post(self):
        args = parser.parse_args()
        name = args['name']
        password = args['password']
        info = args['info']
        user = User(name=name, info=info, password = password)
        db.session.add(user)
        db.session.commit()
        return args['name'], 201


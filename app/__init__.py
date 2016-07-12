#!env/bin/python
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)
from controllers import Users
api.add_resource(Users, '/')
db.create_all()
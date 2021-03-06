#! env/bin/python

from app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = 'users'
    name = db.Column(db.String(32))
    password = db.Column(db.String)
    info = db.Column(db.String(100))
    email = db.Column(db.String(100))
    is_admin = db.Column(db.SmallInteger)



class Task(Base):
    __tablename__ = 'tasks'
    title = db.Column(db.String(32))
    description = db.Column(db.String(100))
    status = db.Column(db.String(10))

class Attachment(Base):
    __tablename__ = 'attachments'
    owner = db.Column(db.String(100))
    file_url = db.Column(db.String(10))
    task_id = db.Column(db.Integer)

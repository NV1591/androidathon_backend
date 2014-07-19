
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    category = db.Column(db.String(120), index = True)
    price = db.Column(db.SmallInteger, default = ROLE_USER)
    rating = db.Column(db.SmallInteger, default = ROLE_USER)
    reviews = db.Column(db.SmallInteger, default = ROLE_USER)
    phone = db.Column(db.String(64), index = True)

    def __repr__(self):
        return '<User %r>' % (self.name)


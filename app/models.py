from app import db


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    reviews = db.Column(db.Integer)
    phone = db.Column(db.String())
    longitude = db.Column(db.String())
    latitude = db.Column(db.String())
    image = db.Column(db.String())

class Consumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    workerid = db.Column(db.Integer)
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    tagline = db.Column(db.String())
    image = db.Column(db.String())

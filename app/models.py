from app import db


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    reviews = db.Column(db.Integer)
    phone = db.Column(db.String())

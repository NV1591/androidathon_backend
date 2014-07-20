from app import app,db
from app import models
db.session.query(models.Category).all()
models.Worker.query.all()

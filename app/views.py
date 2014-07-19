from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from app import app, db
import models

@app.route('/fetch/worker', methods=['GET'])
def get_workers():
    category_ = request.args.get('category')
    filtered_list = models.Worker.query.filter_by(category='Electrician').all()
#    for item in skilled_workers:
 #       if item['category'] == category:
  #          filtered_list.append(item)

    return jsonify({'workers': filtered_list})

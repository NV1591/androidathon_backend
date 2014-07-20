from app import app, db
from flask import Flask, jsonify, request, make_response, abort
from utils import calc_dist, create_dictionary
import unicodedata
from models import Worker, Category
from data import skilled_workers, category_list


@app.route('/migration/worker', methods=['GET'])
def migration_worker():
    for item in skilled_workers:
        worker_object = Worker(name=item['name'],
                               category=item['category'],
                               price=item['category'],
                               rating=item['rating'],
                               reviews=item['reviews'],
                               phone=item['phone'],
                               longitude=item['longitude'],
                               latitude=item['latitude'],
                               image="",)
        db.session.add(worker_object)
        db.session.commit()
    return make_response(jsonify({'error': 'Not found'}))


@app.route('/migration/category', methods=['GET'])
def migration_category():
    for item in category_list:
        worker_object = Category(name=item['name'],
                                 tagline=item['tagline'],
                                 image=item['image'],)
        db.session.add(worker_object)
        db.session.commit()
    return make_response(jsonify({'error': 'Not found'}))


@app.route('/fetch/category', methods=['GET'])
def get_category():
    query = db.session.query(Category).all()
    for item in query:
        awesome_dict = create_category_dictionary(item)
        final_list.append(awesome_dict)

    return jsonify({'category': final_list})


@app.route('/fetch/worker', methods=['GET'])
def get_workers():
    if request:
        app.logger.info('request headers - {0}'.format(request.headers))
    category = request.args.get('category')
    filtered_list = []
    final_list = []
    # query = db.session.query(TweetInfo).filter(TweetInfo.published == TWEET_PUBLISHED).order_by(db.desc(TweetInfo.id))
    query = db.session.query(Worker).all()
    if query:
        app.logger.info('query value true')
    for item in query:
        if item.category == category:
            filtered_list.append(item)

    latitude = request.args.get('latitude')
    unicodedata.normalize('NFKD', latitude).encode('ascii', 'ignore')
    longitude = request.args.get('longitude')
    unicodedata.normalize('NFKD', longitude).encode('ascii', 'ignore')
    distance = request.args.get('distance')

    if not distance:
        distance = 2.0
    for item in filtered_list:
        distance_point = calc_dist(float(item.latitude), float(item.longitude),
                                   float(latitude), float(longitude))
        app.logger.info('dist - {0}'.format(distance_point))
        distance_point = 1.5
        if distance_point < distance:
            awesome_dict = create_dictionary(item, distance_point)
            final_list.append(awesome_dict)

    return jsonify({'workers': final_list})


@app.route('/signup/worker/', methods=['POST'])
def create_worker():
    if not request.json:
        abort(400)
    worker_object = Worker(name=request.json['name'],
                           category=request.json['category'],
                           price=request.json['price'],
                           rating=request.json['rating'],
                           reviews=request.json['reviews'],
                           phone=request.json['phone'],
                           longitude=request.json['longitude'],
                           latitude=request.json['latitude'],
                           image="",)
    db.session.add(worker_object)
    db.session.commit()
    return jsonify({'success': 'worker created'}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

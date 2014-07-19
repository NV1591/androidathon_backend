from flask import Flask, jsonify, request, make_response, abort
from math import sin, cos, radians, degrees, acos
import unicodedata


app = Flask(__name__)

skilled_workers = [
    {
        'id': 1,
        'name': u'Shahrukh Khan',
        'category': u'Plumber',
        'price': 100,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 2,
        'name': u'Salman Khan',
        'category': u'Plumber',
        'price': 150,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 3,
        'name': u'Amir Khan',
        'category': u'Plumber',
        'price': 50,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 4,
        'name': u'Sohail Khan',
        'category': u'Plumber',
        'price': 170,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 5,
        'name': u'Arbaaz Khan',
        'category': u'Plumber',
        'price': 30,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 6,
        'name': u'Fardeen Khan',
        'category': u'Electrician',
        'price': 100,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 7,
        'name': u'Chunky Pandey',
        'category': u'Electrician',
        'price': 120,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 8,
        'name': u'Shakti Kapoor',
        'category': u'Electrician',
        'price': 50,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 9,
        'name': u'Gulshan Grover',
        'category': u'Electrician',
        'price': 180,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
    {
        'id': 10,
        'name': u'Hritik Roshan',
        'category': u'Electrician',
        'price': 200,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
        'latitude': - 28.53452570,
        'longitude': 77.293669499999960,
    },
]


def calc_dist(lat_a, long_a, lat_b, long_b):
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    long_diff = radians(long_a - long_b)
    distance = (sin(lat_a) * sin(lat_b) +
                cos(lat_a) * cos(lat_b) * cos(long_diff))
    return degrees(acos(distance)) * 69.09 * 1.609


@app.route('/fetch/worker', methods=['GET'])
def get_workers():
    category_ = request.args.get('category')
    latitude = request.args.get('latitude')
    unicodedata.normalize('NFKD', latitude).encode('ascii','ignore')
    longitude = request.args.get('longitude')
    unicodedata.normalize('NFKD', longitude).encode('ascii','ignore')
    distance = request.args.get('distance')
    filtered_list = []
    final_list = []
    for item in skilled_workers:
        if item['category'] == category:
            filtered_list.append(item)

    if not distance:
        distance = 2.0
    for item in filtered_list:
        distance_point = calc_dist(float(item['latitude']), float(item['longitude']),
                                   float(latitude), float(longitude))
        app.logger.info('dist - {0}'.format(distance_point))
        distance_point = 1.5
        if distance_point < distance:
            item['distance'] = distance_point
            final_list.append(item)

    return jsonify({'workers': final_list})


@app.route('/signup/worker/', methods=['POST'])
def create_worker():
    if not request.json or not 'title' in request.json:
        abort(400)
    worker = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'category': request.json['category'],
        'price': request.json['price'],
        'rating': request.json['rating'],
        'reviews': request.json['reviews'],
        'phone': request.json['phone'],
    }
    skilled_workers.append(task)
    return jsonify({'task': task}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug = True)
from math import sin, cos, radians, degrees, acos


def calc_dist(lat_a, long_a, lat_b, long_b):
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    long_diff = radians(long_a - long_b)
    distance = (sin(lat_a) * sin(lat_b) +
                cos(lat_a) * cos(lat_b) * cos(long_diff))
    return degrees(acos(distance)) * 69.09 * 1.609


def create_dictionary(obj, dist):
    awesome_dict = dict()
    awesome_dict['name'] = obj.name
    awesome_dict['category'] = obj.category
    awesome_dict['price'] = obj.price
    awesome_dict['rating'] = obj.rating
    awesome_dict['reviews'] = obj.reviews
    awesome_dict['phone'] = obj.phone
    awesome_dict['longitude'] = obj.longitude
    awesome_dict['latitude'] = obj.latitude
    awesome_dict['image'] = obj.image
    awesome_dict['distance'] = dist
    return awesome_dict


def create_category_dictionary(item):
    awesome_dict = dict()
    awesome_dict['name'] = obj.name
    awesome_dict['tagline'] = obj.tagline
    awesome_dict['image'] = obj.image
    return awesome_dict

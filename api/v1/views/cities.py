#!/usr/bin/python3
""" City API actions """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_city_state(state_id):
    """ Retrieves the list of all City objects of a State """
    state = storage.get('State', state_id)
    if state:
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities), 200
    abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['GET'], strict_slashes=False)
def get_city_id(city_id):
    """ Retrieves a City object """
    city = storage.get('City', city_id)
    if city:
        return jsonify(city.to_dict()), 200
    abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(state_id):
    """ Deletes a City object """
    city = storage.get('City', city_id)
    if city:
        city.delete()
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """ Creates a City """
    state = storage.get('State', state_id)
    to_city = request.get_json()
    if not to_city:
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'name' not in to_city:
        return jsonify({'error': 'Missing name'}), 400
    if state:
        to_city['state_id'] = state.id
        city = City(**to_city)
        city.save()
        return jsonify(city.to_dict()), 201
    abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_city(state_id):
    """ Updates a City object """
    to_city = request.get_json()
    if not to_city:
        return jsonify({'error': 'Not a JSON'}), 400
    city = storage.get('City', city_id)
    if city:
        city.name = to_city['name']
        city.save()
        return jsonify(city.to_dict()), 200
    abort(404)

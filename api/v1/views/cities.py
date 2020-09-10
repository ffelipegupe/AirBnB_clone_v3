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
    states = storage.get('State', state_id)
    if states is None:
        abort(404)
    all_cities = storage.all('City')
    city_states = [obj.to_json() for obj in all_cities.values()
                   if obj.state_id == state.id]
    return jsonify(city_states)


@app_views.route('/cities/<city_id>',
                 methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """ Retrieves a City object """
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_json())

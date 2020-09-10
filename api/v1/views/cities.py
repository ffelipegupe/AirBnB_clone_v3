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

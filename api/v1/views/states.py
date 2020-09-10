#!/usr/bin/python3
""" State API actions """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """ Retrieves the list of all State objects """
    state_all = []
    for state in storage.all("State").values():
        state_all.append(state.to_dict())
    return jsonify(state_all)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id=None):
    """ Retrieves a State object """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id=None):
    """ Deletes a State object """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state(state_id):
    """ Creates a State """
    state = request.get_json(silent=True)
    if state is None:
        abort(400, "Not a JSON")
    elif "name" not in state.keys():
        abort(400, "Missing name")
    else:
        new_state = state.State(**state)
        storage.new(new_state)
        storage.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id=None):
    """ Updates a State object """
    lo_js = storage.get("State", state_id)
    if lo_js is None:
        abort(404)
    state = request.get_json(silent=TRUE)
    if state is None:
        abort(400, "Not a JSON")
    else:
        for key, value in state.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(lo_js, key, value)
        storage.save()
        return jsonify(lo_js.to_dict()), 200

import copy

from flask import make_response, jsonify

RESPONSE_STRUCT = {
    'code': 0,
    'data': {},
    'messages': 'Success'
}


def response(data=None):
    response_structure = copy.deepcopy(RESPONSE_STRUCT)
    if data is None:
        data = {}

    response_structure['data'] = data
    return make_response(jsonify(response_structure), 200)

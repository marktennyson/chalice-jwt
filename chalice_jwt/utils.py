from json import dumps

def _jsonify(**kwargs):
    return dumps(kwargs)
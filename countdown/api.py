from time import time

from flask import request

from . import app
from .countdown import Cache


@app.route('/api/v1/<uuid:id>', methods=['GET'])
def get_countdown(id):
    cache = Cache.get_instance()
    countdown = cache.get_countdown(id)

    response = countdown

    time_passed = time() - float(countdown['start'])
    time_left = float(countdown['total']) - time_passed
    response['left'] = time_left
    response['roundtrip_start'] = request.args.get('roundtrip_start')

    return response


@app.route('/api/v1', methods=['POST'])
def create_countdown():
    cache = Cache.get_instance()

    countdown = request.json
    total = float(countdown['total'])
    response = cache.add_countdown(total)
    return response


@app.route('/api/v1/start/<uuid:id>', methods=['PATCH'])
def start_countdown(id):
    cache = Cache.get_instance()
    return cache.start_countdown(id)


@app.route('/api/v1/reset/<uuid:id>', methods=['PATCH'])
def reset_countdown(id):
    cache = Cache.get_instance()
    return cache.reset_countdown(id)


@app.route('/api/v1/stop/<uuid:id>', methods=['PATCH'])
def stop_countdown(id):
    cache = Cache.get_instance()
    return cache.stop_countdown(id)

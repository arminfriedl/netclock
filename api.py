from flask import request, jsonify
from walrus import Walrus
from time import time

import uuid
import struct

from countdown import api_api

db = Walrus(host='localhost', port=6379, db=0)

@app.route('/api/vi1/<uuid:id>', methods=['GET'])
def get_countdown(id):
    ct = db.Hash(str(id))

    resp = ct.as_dict(decode=True)
    resp['left'] = float(ct['total']) - (time() - float(ct['start']))

    return resp

@api_v1.route('/api/v1', methods=['POST'])
def create_countdown():
    countdown = request.json
    ct_id = str(uuid.uuid4())
    ct = db.Hash(ct_id)
    ct.update(start=time(), total=countdown['total'])

    resp = ct.as_dict(decode=True)
    resp['id'] = ct_id

    return resp

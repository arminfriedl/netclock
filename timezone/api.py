from flask import request, jsonify
from time import time

import uuid
import struct

from . import app

@app.route('/api/v1/autocomplete', methods=['GET'])
def autocomplete_timezone():
    complete_str = request.args.get('complete')
    if not complete_str: return "No part"

    return complete_str


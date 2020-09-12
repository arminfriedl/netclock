from flask import Blueprint

api_v1 = Blueprint('api.v1', __name__)

import api.v1.clock
import api.v1.countdown


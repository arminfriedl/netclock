from flask import Flask
app = Flask(__name__)

from api.v1 import api_v1
app.register_blueprint(api_v1, url_prefix="/api/v1")

import views

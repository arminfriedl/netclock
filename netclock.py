from flask import Flask
app = Flask(__name__)

from countdown import app as countdown
app.register_blueprint(countdown, url_prefix="/countdown")

import views

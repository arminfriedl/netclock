from flask import Flask

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.update(SESSION_COOKIE_SAMESITE='Strict')

from countdown import app as countdown

app.register_blueprint(countdown, url_prefix="/countdown")

from worldclock import app as worldclock

app.register_blueprint(worldclock, url_prefix="/worldclock")

from timezone import app as timezone

app.register_blueprint(timezone, url_prefix="/timezone")

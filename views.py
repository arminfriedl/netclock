from flask import render_template

from netclock import app


@app.route('/')
def index():
    return render_template('netclock.html')

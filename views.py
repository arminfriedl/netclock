from flask import Flask, render_template, request, flash
from netclock import app

from forms import CountdownAdminForm

@app.route('/')
def index():
    return render_template('netclock.html')


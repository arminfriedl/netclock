from flask import Flask, render_template, request, flash
from netclock import app

@app.route('/')
def index():
    breakpoint()

    return render_template('netclock.html')


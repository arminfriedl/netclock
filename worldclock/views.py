from flask import render_template, request, flash, redirect, url_for, session

from . import app

@app.route('', methods=['GET'])
def create():
    return render_template("worldclock/create.html")

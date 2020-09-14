from flask import render_template, request, flash, redirect, url_for, session

from . import app

@app.route('', methods=['GET'])
def create_get():
    return "Bye"

@app.route('', methods=['POST'])
def create_post():
    return "Hello"

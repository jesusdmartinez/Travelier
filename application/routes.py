from flask import current_app as app
from flask import render_template, jsonify, flash, request

from .hello import HelloApi
from .models import User

from . import db


app.register_blueprint(HelloApi, url_prefix='/hello')


@app.route('/')
def hello():
    return render_template('hello.html')

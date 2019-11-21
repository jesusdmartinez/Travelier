from flask import current_app as app
from flask import render_template, jsonify, flash, request

from .users import NewUsersApi
from .questions import NewQuestionApi

from .models import Questions, User, Answers

from . import db

app.register_blueprint(NewUsersApi, url_prefix='/')
app.register_blueprint(NewQuestionApi, url_prefix='/question')



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/question', methods=['POST'])
def create_question():
    try:
        new_question = Questions.create_question(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400
    db.session.add(new_question)
    db.session.commit()
    return jsonify(), 200



@app.route('/answer', methods=['POST'])
def create_answer():
    try:
        new_answer = Answers.create_answer(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400
    db.session.add(new_answer)
    db.session.commit()
    return jsonify(), 200

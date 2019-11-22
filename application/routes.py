from flask import current_app as app
from flask import render_template, jsonify, flash, request

from .users import NewUsersApi
from .questions import NewQuestionApi

from .models import Questions, User, Answers

from . import db

app.register_blueprint(NewUsersApi, url_prefix='/')
app.register_blueprint(NewQuestionApi, url_prefix='/question')


# Home page --> 5 section scrolling site with top portion dedicated to creating a trip
@app.route('/')
def home():
    return render_template('home.html')


# Get Started Page --> Sheet 1 of questionnaire
@app.route('/get-started')
def get_started():
    return render_template('get-started.html')


# Brazil Page --> Page to display different trip options in brazil
@app.route('/brazil')
def brazil():
    return render_template('brazil.html')



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

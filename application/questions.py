from flask import Blueprint, jsonify, request, render_template
from . import db
from .models import Questions

NewQuestionApi = Blueprint('new_question', __name__)

@NewQuestionApi.route('/question', methods=['POST'])
def create_question():
    try:
        new_question = Questions.create_question(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400
    db.session.add(new_question)
    db.session.commit()
    return jsonify(), 200


@NewQuestionApi.route('<question_id>', methods=['GET'])
def get_question(question_id):
    question = Questions.query.filter(Questions.question_id == question_id).first()
    if question is None:
        return 'question id not found', 404
    return jsonify(question.return_question()), 200
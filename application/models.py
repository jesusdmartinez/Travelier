from . import db, login
from datetime import datetime
from sqlalchemy import Table, Integer, String, ForeignKey, Column, ForeignKeyConstraint, VARCHAR
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.VARCHAR(11), unique=True, nullable=False)
    signup_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @staticmethod
    def create_user(dict):
        return User(first_name=dict['first_name'], last_name=dict['last_name'], email=dict['email'], phone_number=dict['phone_number'])

    def retrieve_users(self):
        return {
           'user_id': self.user_id,
           'first_name': self.first_name,
           'last_name': self.last_name,
           'email': self.email,
           'phone_number': self.phone_number,
       }



class Questions(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    question = db.Column(db.String(250), nullable=False, unique=False)

    @staticmethod
    def create_question(dict):
        return Questions(question=dict['question'])

    def return_question(self):
        return {
            'question_id': self.question_id,
           'question': self.question,
       }



class Answers(db.Model):
    __tablename__ = 'answers'
    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete="SET NULL"))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id', ondelete="SET NULL"))
    answer = db.Column(db.String(250), nullable=False, unique=False)
    answer_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)

    @staticmethod
    def create_answer(dict):
        return Answers(user_id=dict['user_id'], question_id=dict['question_id'], answer=dict['answer'])

    def return_answer(self):
        return {
            'answer_id': self.answer_id,
            'user_id': self.user_id,
            'question_id': self.question_id,
            'answer': self.answer,
       }

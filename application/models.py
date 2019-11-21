from . import db
from datetime import datetime
from sqlalchemy import Table, Integer, String, ForeignKey, Column, ForeignKeyConstraint, VARCHAR


# Do I need to make an association table here?  Could simply use a normal class, and incorporate staticmethods to create, too?
user_question_answer = Table('user_question_answer', db.Model.metadata,
                             db.Column('user_id', db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE')),
                             db.Column('question_id', db.Integer, db.ForeignKey('questions_answers.question_id', ondelete='CASCADE')),
                             db.Column('answer_id', db.Integer, db.ForeignKey('questions_answers.answer_id', ondelete='CASCADE')))


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.VARCHAR(11), unique=True, nullable=False)
    signup_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)


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
    answer = db.Column(db.String(250), nullable=False, unique=False)
    # user = db.relationship('User', foreign_keys=user_id)

    @staticmethod
    def create_answer(dict):
        return Answers(question_id=dict['question_id'], answer=dict['answer'])

    def return_answer(self):
        return {
            'answer_id': self.answer_id,
            'question_id': self.question_id,
            'answer': self.answer,
            'user': self.users.retrieve_users()
       }


# Do I need the table below AND the association table at the top of code?  It seems repetitive.
class QuestionsAnswers(db.Model):
    __tablename__ = 'questions_answers'
    questions_answers_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id',
                                                      ondelete="SET NULL"))
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.answer_id',
                                                      ondelete="SET NULL"))

    @staticmethod
    def create_question_answer(dict):
        return QuestionsAnswers(question_id=dict['question_id'], answer_id=dict['answer_id'])

    def return_question(self):
        return {
            'questions_answers_id': self.questions_answers_id,
            'question_id': self.question_id,
            'answer_id': self.answer_id,
       }

from flask import current_app as app
from flask import render_template, jsonify, flash, request, redirect, url_for
from flask_login import current_user, login_user

from .users import NewUsersApi
from .questions import NewQuestionApi

from .models import Questions, User, Answers
from .forms import LoginForm

from . import db

app.register_blueprint(NewUsersApi, url_prefix='/')
app.register_blueprint(NewQuestionApi, url_prefix='/question')


# Home page --> 5 section scrolling site with top portion dedicated to creating a trip
@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Jesus'}
    posts = [
        {
            'author': {'username': 'Jonah'},
            'body': 'I love Brazilian Women'
        },
        {
            'author': {'username': 'Patrick'},
            'body': 'I love Taiwan'
        },
        {
            'author': {'username': 'Jesus'},
            'body': 'Lets kitesurf in Mexico, G'
        }
    ]
    return render_template('home.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(first_name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)







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

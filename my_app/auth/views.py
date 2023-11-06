from flask import request, render_template, flash, redirect, url_for, session, Blueprint, g
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_login import login_manager, current_user, login_required, logout_user, login_user

from my_app import db, app
from my_app.auth.models import User, RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/')
@auth.route('/home')
def home():
    return render_template('home.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('username'):
        flash('Jesteś zalogowany', 'info')
        return redirect(url_for('auth.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash('Ten użytkownik już istnieje', 'warning')
            return render_template('register.html', form=form)
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        flash('Jesteś zarejestowany', 'success')
        return redirect(url_for('auth.login'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Jesteś zalogowany', 'info')
        return redirect(url_for('auth.home'))
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()
        if not (existing_user and existing_user.check_password(password)):
            flash('Błędne dane uwierzytelnienia', 'danger')
            return render_template('login.html', form=form)
        session['username'] = username
        flash('Jesteś zalogowany', 'success')
        return redirect(url_for('auth.home'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))


@login_manager.user_accessed
def load_user(id):
    return User.query.get(int(id))


@auth.before_request
def get_current_user():
    g.user = current_user


facebook_blueprint = make_facebook_blueprint(scope='email', redirect_to='auth.facebook_login')


@auth.route('/facebook-login')
def facebook_login():
    if not facebook.authorized:
        return redirect(url_for('facebook.login'))
    resp = facebook.get("/me?fields=name,email")
    user = User.query.filter_by(username=resp.json()['email'].first())
    if not user:
        user = User(resp.json()['email'], '')
        db.session.add(user)
        db.session.commit()
    login_user()
    flash("Zalogowano przez facebook", 'success')
    return redirect(request.args.get('next', url_for('auth.home')))

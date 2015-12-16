# Import flask dependencies
from flask import Blueprint, request, render_template, session, redirect, url_for

# Import app object for sharing
from app import app

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import *

# import flask_admin as admin
import flask_login as login
# from flask_admin.contrib.mongoengine import ModelView
# from flask_admin import helpers


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
# login
@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    # If sign in form is submitted
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = form.get_user()
            app.login.login_user(user)
            return redirect('/')

    return render_template('auth/signin.html', form=form)

# logout
@mod_auth.route('/logout', methods=('GET', 'POST'))
def logout():
    app.login.logout_user()
    return redirect('/auth/login')

# sign up
@mod_auth.route('/signup', methods=('GET', 'POST'))
def signup():
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User()

            form.populate_obj(user)
            user.save()

            app.login.login_user(user)
            return redirect('/')

    return render_template('auth/signup.html', form=form)


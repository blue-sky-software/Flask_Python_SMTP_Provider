# Import flask dependencies
from flask import Blueprint, request, render_template, session, redirect, url_for

# Import app object for sharing
from app import app

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# import flask_admin as admin
import flask_login as login
# from flask_admin.contrib.mongoengine import ModelView
# from flask_admin import helpers


# Define the blueprint: 'stat', set its url prefix: app.url/stat
mod_stat = Blueprint('stat', __name__, url_prefix='/stat')

# Set the route and accepted methods
# login
@mod_stat.route('/', methods=['GET', 'POST'])
def stat():

    # if request.method == 'POST':
    #     if form.validate():
    #         user = form.get_user()
    #         app.login.login_user(user)
    #         return redirect('/')

    data = ''
    return render_template('stat/stat.html', data=data, nav=2)
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


# Define the blueprint: 'suppressions', set its url prefix: app.url/suppressions
mod_suppressions = Blueprint('suppressions', __name__, url_prefix='/suppressions')

# Set the route and accepted methods
# bounces
@mod_suppressions.route('/bounces', methods=['GET', 'POST'])
def bounces():
    data = ''
    return render_template('suppressions/bounces.html', data=data, nav=31)

# unsubscribes
@mod_suppressions.route('/unsubscribes', methods=['GET', 'POST'])
def unsubscribes():
    data = ''
    return render_template('suppressions/unsubscribes.html', data=data, nav=32)

# spamreports
@mod_suppressions.route('/spamreports', methods=['GET', 'POST'])
def spamreports():
    data = ''
    return render_template('suppressions/spamreports.html', data=data, nav=33)

# manual
@mod_suppressions.route('/manual', methods=['GET', 'POST'])
def manual():
    data = ''
    return render_template('suppressions/manual.html', data=data, nav=34)
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


# Define the blueprint: 'settings', set its url prefix: app.url/settings
mod_settings = Blueprint('settings', __name__, url_prefix='/settings')

# Set the route and accepted methods
# tracking
@mod_settings.route('/tracking', methods=['GET', 'POST'])
def tracking():
    data = ''
    return render_template('settings/tracking.html', data=data, nav=41)

# apikey
@mod_settings.route('/apikey', methods=['GET', 'POST'])
def apikey():
    data = ''
    return render_template('settings/apikey.html', data=data, nav=42)

# alerts
@mod_settings.route('/alerts', methods=['GET', 'POST'])
def alerts():
    data = ''
    return render_template('settings/alerts.html', data=data, nav=43)

# credentials
@mod_settings.route('/credentials', methods=['GET', 'POST'])
def manual():
    data = ''
    return render_template('settings/credentials.html', data=data, nav=44)

# spamprotection
@mod_settings.route('/spamprotection', methods=['GET', 'POST'])
def spamprotection():
    data = ''
    return render_template('settings/spamprotection.html', data=data, nav=45)

# billing
@mod_settings.route('/billing', methods=['GET', 'POST'])
def billing():
    data = ''
    return render_template('settings/billing.html', data=data, nav=46)
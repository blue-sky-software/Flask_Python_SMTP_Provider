# Import flask and template operators
from flask import Flask, render_template
from flask_mongoengine import MongoEngine

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = MongoEngine()
db.init_app(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('dashboard/index.html', user=app.login.current_user, nav=1)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_stat.controllers import mod_stat as stat_module
from app.mod_suppressions.controllers import mod_suppressions as suppressions_module
from app.mod_settings.controllers import mod_settings as settings_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(stat_module)
app.register_blueprint(suppressions_module)
app.register_blueprint(settings_module)

# Build the database:

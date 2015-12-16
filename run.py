# Run a test server.
from app import app
from app.mod_auth.models import User
import flask_login as login
from flask import g

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.setup_app(app)
    app.login = login

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()

if __name__ == '__main__':

    # import logging
    # logging.basicConfig(filename='error.log', level=logging.DEBUG)

    # initialize of login object
    init_login()

    # Start app
    app.run()
    # app.run(host='127.0.0.1', port=5000, debug=True)
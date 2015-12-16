# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


# Define a User model
class User(db.Document):

    __tablename__ = 'auth_user'

    # User Name
    name     = db.StringField(max_length=128,  nullable=False, unique=True)

    # Identification Data: email & password
    email    = db.EmailField(max_length=128,  nullable=False, unique=True)
    password = db.StringField(max_length=40,  nullable=False)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    # Required for administrative interface
    def __unicode__(self):
        return self.name
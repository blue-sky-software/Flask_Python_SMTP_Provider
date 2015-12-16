# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import form, BooleanField, TextField, PasswordField, validators

# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the login form (WTForms)
# LoginForm
class LoginForm(form.Form):
    name = TextField(validators=[validators.required()])
    password = PasswordField(validators=[validators.required()])

    def validate_name(self, field):
        user = self.get_user()

        if user is None or user.password != self.password.data:
            raise validators.ValidationError('Invalid username or password')

    def get_user(self):
        return User.objects(name=self.name.data).first()

# RegistrationForm
class RegistrationForm(form.Form):
    name = TextField(validators=[validators.required()])
    email = TextField(validators=[validators.email(), validators.required()])
    password = PasswordField(validators=[validators.required()])

    def validate_name(self, field):
        if User.objects(name=self.name.data):
            raise validators.ValidationError('Duplicate username')
            return False
        return True

    def validate_email(self, field):
        if User.objects(email=self.email.data):
            raise validators.ValidationError('Duplicate emailaddress')
            return False
        return True
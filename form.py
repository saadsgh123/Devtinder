from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class RegisterForm(FlaskForm):
    debug = True
    fname = StringField(
        'First Name',
        validators=[DataRequired(message="First name is required"), Length(min=2, max=25)]
    )
    lname = StringField(
        'Last Name',
        validators=[DataRequired(message="Last name is required"), Length(min=2, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(message="Email is required"), Email(message="Invalid email address")]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Password is required"), Regexp(
            r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
            message="Password must be at least 8 characters long and contain a letter, number, and special character"
        )]
    )
    repeat_password = PasswordField(
        'Repeat Password',
        validators=[DataRequired(message="Please confirm your password"), EqualTo('password', message="Passwords must match")]
        )

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('login')

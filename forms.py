from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CreateUser(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=40)])
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Create User')


class WritePost(FlaskForm):
    username = SelectField('Username', choices=[], validators=[DataRequired()])
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=2, max=30)])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Write Post')


class DeleteUser(FlaskForm):
    user = SelectField('Username', choices=[], validators=[DataRequired()])
    submit = SubmitField('Delete User')

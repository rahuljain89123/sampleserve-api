
from flask.ext.wtf import FlaskForm

from wtforms import TextField, PasswordField, validators, TextAreaField, SelectField, SelectMultipleField, HiddenField, RadioField, BooleanField, FileField
from wtforms.validators import DataRequired, ValidationError, Required, Optional, Length, URL, Email


class InquiryForm(FlaskForm):
    name = TextField('Name', validators=[Required()])
    company_name = TextField('Company Name', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email()])
    phone = TextField('Phone number', validators=[Optional()])
    number_of_employees = TextField('Number of Employees', validators=[Optional()])

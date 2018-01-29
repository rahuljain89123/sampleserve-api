
from flask.ext.wtf import FlaskForm

from wtforms import TextField, PasswordField, validators, TextAreaField, SelectField, SelectMultipleField, HiddenField, RadioField, BooleanField, FileField
from wtforms.validators import DataRequired, ValidationError, Required, Optional, Length, URL, Email, Regexp

from sampleserve.models import Lab
from sampleserve.reports.helpers import slugify


class OnboardLabForm(FlaskForm):
    lab_name = TextField('Lab Name', validators=[Required(), Length(min=4)])
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email()])

    def validate_lab_name(form, field):
        subdomain = slugify(field.data)
        existing_lab = Lab.query.filter_by(url=subdomain).first()
        if existing_lab:
            raise ValidationError("Lab with subdomain %s already exists. Please try another." % subdomain)

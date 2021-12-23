from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
import re

class QueryForm(FlaskForm):
    search = StringField('Enter domain', validators=[DataRequired()])

    def validate_search(form, field):
        if not re.match(r'[A-z0-9\-\.]+\.[A-z0-9\-\.]+', str(field.data)):
            raise ValidationError(f"Invalid domain: '{field.data}'")

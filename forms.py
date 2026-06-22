from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    Address = StringField('Address', validators=[DataRequired()])
    Age = IntegerField('Age', validators=[DataRequired()])
    Gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], validators=[DataRequired()])

    submit = SubmitField('Confirm Booking')
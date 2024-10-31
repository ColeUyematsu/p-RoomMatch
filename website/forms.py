# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class QuestionnaireForm(FlaskForm):
    question1 = IntegerField('Rate your experience with coding (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    question2 = StringField('Preferred programming language?', validators=[DataRequired()])
    question3 = TextAreaField('Tell us about a recent project', validators=[DataRequired()])
    submit = SubmitField('Submit')
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class QuestionnaireForm(FlaskForm):
    follow_schedule = IntegerField(
        'How strictly do you follow a schedule? (1 = Rarely, 10 = All the time)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    guests_comfort = IntegerField(
        'How comfortable are you with having guests stay over? (1 = Not comfortable at all, 10 = Very comfortable)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    romantic_focus = IntegerField(
        'How much do you currently focus on romantic relationships? (1 = Not at all, 10 = Very often)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    music_enjoyment = IntegerField(
        'How much do you enjoy different music genres (e.g., rap, pop, country)? (1 = Dislike, 10 = Love)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    packing_amount = IntegerField(
        'How much are you planning to pack for school? (1 = Packing very little, 10 = Packing a lot)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    tv_importance = IntegerField(
        'How important is it for you to have a TV in your room? (1 = Not important, 10 = Very important)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    study_social = IntegerField(
        'How well do you study in environments with social activity? (1 = Not well at all, 10 = Very well)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    commitments_sleep = IntegerField(
        'How often might commitments such as athletics/clubs impact your sleep schedule? (1 = Never, 10 = Almost everyday)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    travel_offcampus = IntegerField(
        'How often do you travel or go off-campus? (1 = Rarely, 10 = Very frequently)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    roommate_bedtime = IntegerField(
        'How important is it for you to go to bed around the same time as your roommate? (1 = Not important, 10 = Very important)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    binge_tv = IntegerField(
        'How frequently do you watch or binge TV shows or movies? (1 = Rarely, 10 = Very often)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    similar_major_importance = IntegerField(
        'How important is it for you to room with someone in a similar major or classes? (1 = Not important, 10 = Very important)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    quiet_hours = IntegerField(
        'How do you feel about quiet hours? (1 = Don’t like them, 10 = Very important)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    alarm_time = IntegerField(
        'What time is your most regularly used alarm set (or general wake up time if you don’t use alarms)? (1 = Before 6 am, 5 = About 9 pm, 10 = After 12 pm)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    smoke_drink = IntegerField(
        'How often do you recreationally smoke or drink? (1 = Never, 10 = Very often)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    appliances_usage = IntegerField(
        'How often do you use blow dryers or other noticeable appliances? (1 = Rarely, 10 = Very often)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    guests_frequency = IntegerField(
        'How often do you expect to have guests over? (1 = Rarely, 10 = Very frequently)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    room_decoration = IntegerField(
        'How much do you like to decorate your room? (1 = Not at all, 10 = Very much)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    roommate_closeness = IntegerField(
        'How close would you like to be with your roommate? (1 = Just coexisting, 10 = Very close friends)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    family_visits = IntegerField(
        'How often do you expect your family to visit? (1 = Rarely, 10 = Very frequently)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    laundry_frequency = IntegerField(
        'How often do you do your own laundry? (1 = Rarely, 10 = Very often)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    activity_priorities = IntegerField(
        'How would you prioritize the following activities: work, play, cleaning, and rest? (Rank each from 1 to 10)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    social_events = IntegerField(
        'How likely are you to go out to social events each week? (1 = Never, 10 = Several times a week)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    bedtime_weekdays = IntegerField(
        'How early do you go to bed on weekdays? (1 = Before 9 PM, 10 = After 2 AM)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    noise_level = IntegerField(
        'How much noise do you usually make in your room (e.g., music, talking, gaming)? (1 = Silent, 10 = Very loud)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    room_absence = IntegerField(
        'How often do you think you will be out of the room? (1 = Rarely leave, 10 = Out most of the time)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    ideal_temperature = IntegerField(
        'What is your ideal room temperature? (1 = Very cold, 10 = Very warm)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    windows_open = IntegerField(
        'How often do you like the windows to be open? (1 = Never, 10 = All the time)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    sleep_flexibility = IntegerField(
        'How flexible are you with your roommate having different sleep/wake schedules? (1 = Not flexible at all, 10 = Very flexible)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    guest_curfew = IntegerField(
        'Would you like to have an agreed-upon curfew for guests? (1 = No curfew, 10 = Strict curfew)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    neighbors_importance = IntegerField(
        'How important is it for you to know your neighbors? (1 = Not important, 10 = Very important)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    eat_room = IntegerField(
        'How often do you eat in your room? (1 = Never, 10 = Very frequently)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    conflict_handling = IntegerField(
        'When faced with conflict, how directly do you handle it? (1 = Avoid it, 10 = Address it directly)',
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    submit = SubmitField('Submit')

# class QuestionnaireForm(FlaskForm):
#     question1 = IntegerField('Rate your experience with coding (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
#     question2 = StringField('Preferred programming language?', validators=[DataRequired()])
#     question3 = TextAreaField('Tell us about a recent project', validators=[DataRequired()])
#     submit = SubmitField('Submit')
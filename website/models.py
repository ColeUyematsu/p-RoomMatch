from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  # Relationship to notes created by the user
    questionnaire_response = db.relationship('QuestionnaireResponse', backref='user', uselist=False)
    is_admin = db.Column(db.Boolean, default=False)  # Field to determine admin access to database


class QuestionnaireResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Dynamically defining the columns
    fields = {
        'follow_schedule': db.Integer,
        'guests_comfort': db.Integer,
        'romantic_focus': db.Integer,
        'music_enjoyment': db.Integer,
        'packing_amount': db.Integer,
        'tv_importance': db.Integer,
        'study_social': db.Integer,
        'commitments_sleep': db.Integer,
        'travel_offcampus': db.Integer,
        'roommate_bedtime': db.Integer,
        'binge_tv': db.Integer,
        'similar_major_importance': db.Integer,
        'quiet_hours': db.Integer,
        'alarm_time': db.Integer,
        'smoke_drink': db.Integer,
        'appliances_usage': db.Integer,
        'guests_frequency': db.Integer,
        'room_decoration': db.Integer,
        'roommate_closeness': db.Integer,
        'family_visits': db.Integer,
        'laundry_frequency': db.Integer,
        'activity_priorities': db.Integer,
        'social_events': db.Integer,
        'bedtime_weekdays': db.Integer,
        'noise_level': db.Integer,
        'room_absence': db.Integer,
        'ideal_temperature': db.Integer,
        'windows_open': db.Integer,
        'sleep_flexibility': db.Integer,
        'guest_curfew': db.Integer,
        'neighbors_importance': db.Integer,
        'eat_room': db.Integer,
        'conflict_handling': db.Integer,
    }

    # Dynamically creating class attributes with nullable=True
    locals().update({field: db.Column(data_type, nullable=True) for field, data_type in fields.items()})

    def __init__(self, user_id, **kwargs):
        self.user_id = user_id
        for field in self.fields:
            setattr(self, field, kwargs.get(field))


# class QuestionnaireResponse(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     question1 = db.Column(db.Integer, nullable=False)  # Example: Rating scale question
#     question2 = db.Column(db.String(100), nullable=False)  # Example: Text input for preferred programming language
#     question3 = db.Column(db.Text, nullable=False)  # Example: Textarea for recent project description
#
#     # Constructor for initializing the fields
#     def __init__(self, user_id, question1, question2, question3):
#         self.user_id = user_id
#         self.question1 = question1
#         self.question2 = question2
#         self.question3 = question3


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


class QuestionnaireResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question1 = db.Column(db.Integer, nullable=False)  # Example: Rating scale question
    question2 = db.Column(db.String(100), nullable=False)  # Example: Text input for preferred programming language
    question3 = db.Column(db.Text, nullable=False)  # Example: Textarea for recent project description

    # Constructor for initializing the fields
    def __init__(self, user_id, question1, question2, question3):
        self.user_id = user_id
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3


# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func
#
#
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     notes = db.relationship('Note')

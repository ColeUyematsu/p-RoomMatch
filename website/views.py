from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, QuestionnaireResponse
from . import db
import json
from .forms import QuestionnaireForm  # Import the questionnaire form

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')  # Gets the note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  # Schema for the note
            db.session.add(new_note)  # Add the note to the database
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)  # This function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    form = QuestionnaireForm()
    # Check if the user already has a response
    existing_response = QuestionnaireResponse.query.filter_by(user_id=current_user.id).first()

    if form.validate_on_submit():
        # Update if response exists, else create a new one
        if existing_response:
            existing_response.question1 = form.question1.data
            existing_response.question2 = form.question2.data
            existing_response.question3 = form.question3.data
            flash('Your questionnaire responses have been updated!', 'success')
        else:
            new_response = QuestionnaireResponse(
                user_id=current_user.id,
                question1=form.question1.data,
                question2=form.question2.data,
                question3=form.question3.data
            )
            db.session.add(new_response)
            flash('Thank you for completing the questionnaire!', 'success')

        db.session.commit()
        return redirect(url_for('views.home'))  # Redirect to home or another page

    # Pre-fill the form if there are existing responses
    if existing_response:
        form.question1.data = existing_response.question1
        form.question2.data = existing_response.question2
        form.question3.data = existing_response.question3

    return render_template("questionnaire.html", form=form, user=current_user)


@views.route('/questionnaire/view')
@login_required
def view_questionnaire():
    response = QuestionnaireResponse.query.filter_by(user_id=current_user.id).first()
    if not response:
        flash('You have not completed the questionnaire yet.', 'warning')
        return redirect(url_for('views.questionnaire'))
    return render_template('view_questionnaire.html', response=response, user=current_user)


# from flask import Blueprint, render_template, request, flash, jsonify
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# import json
#
# views = Blueprint('views', __name__)
#
#
# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')#Gets the note from the HTML
#
#         if len(note) < 1:
#             flash('Note is too short!', category='error')
#         else:
#             new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note
#             db.session.add(new_note) #adding the note to the database
#             db.session.commit()
#             flash('Note added!', category='success')
#
#     return render_template("home.html", user=current_user)
#
#
# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
#
#     return jsonify({})

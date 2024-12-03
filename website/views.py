from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import QuestionnaireResponse
from . import db
import json
from .forms import QuestionnaireForm  # Import the questionnaire form

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    form = QuestionnaireForm()
    # Check if the user already has a response
    existing_response = QuestionnaireResponse.query.filter_by(user_id=current_user.id).first()

    if form.validate_on_submit():
        if existing_response:
            # Update existing response with all fields dynamically
            for field in QuestionnaireResponse.fields.keys():
                setattr(existing_response, field, getattr(form, field).data)
            flash('Your questionnaire responses have been updated!', 'success')
        else:
            # Create a new response with all fields dynamically
            new_response = QuestionnaireResponse(
                user_id=current_user.id,
                **{field: getattr(form, field).data for field in QuestionnaireResponse.fields.keys()}
            )
            db.session.add(new_response)
            flash('Thank you for completing the questionnaire!', 'success')

        db.session.commit()
        return redirect(url_for('views.home'))  # Redirect to home or another page

    # Pre-fill the form if there are existing responses
    if existing_response:
        for field in QuestionnaireResponse.fields.keys():
            getattr(form, field).data = getattr(existing_response, field)

    return render_template("questionnaire.html", form=form, user=current_user)

@views.route('/questionnaire/view')
@login_required
def view_questionnaire():
    response = QuestionnaireResponse.query.filter_by(user_id=current_user.id).first()
    if not response:
        flash('You have not completed the questionnaire yet.', 'warning')
        return redirect(url_for('views.questionnaire'))

    # Dynamically collect all fields for the template
    response_data = {field: getattr(response, field) for field in QuestionnaireResponse.fields.keys()}
    return render_template('view_questionnaire.html', response=response_data, user=current_user)

# New About Route
@views.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
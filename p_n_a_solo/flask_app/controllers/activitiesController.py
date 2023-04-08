from pprint import pprint
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.users import User
from flask_app.models.activities import Activity


### ROUTE to the new activity form WORKING
@app.route('/getoutside/activities/new')
def new_activity_form():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("activity_form.html")


### Route to post new activity WORKING
@app.route('/getoutside/activities/new', methods=["POST"])
def create_activity_form_action():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    if not Activity.validate_activity(request.form):
        return redirect('/getoutside/activities/new')  #redirect to where the form is rendered if validation fails
    Activity.create_activity_form_action(request.form) # else save form
    return redirect("/getoutside/athlete") 


### Route for creating update form page WORKING
@app.route('/getoutside/activity/<int:id>/edit')
def edit_activity_by_id(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id': id,
    }
    user ={
        'id': session['user_id']
    }
    return render_template("edit_activity.html", activity = Activity.one_activity_by_id(data), user = User.get_user_by_id(user))


### Route to post new activity                                    TESTING
@app.route('/getoutside/activity/<int:id>/edit', methods=["POST"])
def edit_activity_form_action(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        "id" : id,
        "activity" : request.form["activity"],
        "location" : request.form["location"],
        "date" : request.form["date"],
        }

    if not Activity.validate_activity(data):
        return redirect(f'/getoutside/activity/{id}/edit')  #redirect to where the form is rendered if validation fails
    Activity.update_activity_form_action(data) # else save form
    return redirect(f'/getoutside/activity/{id}') 


### Route To View One Activity  WORKING
@app.route('/getoutside/activity/<int:id>')
def view_one_activity(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id': id,
    }
    user ={
        'id': session['user_id']
    }
    return render_template("one_activity.html", activity = Activity.one_activity_by_id(data), user = User.get_user_by_id(user),attenders = Activity.get_all_attendees(data))


### Join Activity return to main dash WORKING
@app.route('/getoutside/activity/<int:id>/join')
def join_activity_return_to_home_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'activity_id' : id,
        'user_id' : session['user_id']
    }
    Activity.join_activity(data)
    return redirect("/getoutside")


### Join Activity return to user dash WORKING
@app.route('/getoutside/activity/<int:id>/join2')
def join_activity_return_to_activity_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'activity_id' : id,
        'user_id' : session['user_id']
    }
    Activity.join_activity(data)
    return redirect(f"/getoutside/activity/{id}")


### UN Join Activity WORKING
@app.route('/getoutside/activity/<int:id>/unjoin')
def unjoin_activity(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'activity_id' : id,
        'user_id' : session['user_id']
    }
    Activity.unjoin_activity(data)
    return redirect("/getoutside")


### Delete Activity by id  WORKIMG
@app.route('/getoutside/activity/<int:id>/delete')
def delete_activity_by_id(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id,
    }
    Activity.delete_activity_by_id(data)
    return redirect("/getoutside")






### ROUTE FOR FRIENDS PAGE                            /////////// save this for later!!
# @app.route('/dashboard/friends')
# def all_users():
#     if 'user_id' not in session:
#         msg = "you must be logged in!"
#         return redirect('/logout')
#     data ={
#         'id': session['user_id']
#     }
#     return render_template("user_friends.html", friends = User.get_friends(data),user = User.get_user_by_id(data)) ### This should be a joined list and all friends by id

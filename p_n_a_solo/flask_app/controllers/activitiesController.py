from pprint import pprint
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.users import User
from flask_app.models.activities import Activity


### ROUTE FOR ACTIVITY DASH BOARD
@app.route('/getoutside')
def activity_dashboard():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template(
        "activity_dashboard.html", user = User.get_user_by_id(data), activities = Activity.all_activities_with_joined_activities(data))
        # activities = Activity.all_activities(), 
        # joined = Activity.all_joined()


### ROUTE TO NEW ACTIVITY FORM
@app.route('/getoutside/activities/new')
def new_activity_form_page():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("activity_new_form.html")


### NEW ACTIVITY POST ACTION ROUTE WORKING
@app.route('/getoutside/activities/new', methods=["POST"])
def create_activity_form_action():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    if not Activity.activity_validation(request.form):
        return redirect('/getoutside/activities/new')  #redirect to where the form is rendered if validation fails
    Activity.create_activity_form_action(request.form) # else save form
    return redirect("/getoutside/athlete") 


### ROUTE TO UPDATE ACTIVITY FORM
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
    return render_template("activity_edit_form.html", activity = Activity.one_activity_by_id(data), user = User.get_user_by_id(user))


### POST ACTION ROUTE TO UPDATE ACTIVITY
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

    if not Activity.activity_validation(data):
        return redirect(f'/getoutside/activity/{id}/edit') 
    Activity.update_activity_form_action(data) 
    return redirect(f'/getoutside/activity/{id}') 


### VIEW ONE ACTIVITY BY ID
@app.route('/getoutside/activity/<int:id>')
def view_one_activity_by_id(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id': id,
    }
    user ={
        'id': session['user_id']
    }
    return render_template("activity_one_view.html", activity = Activity.one_activity_by_id(data), user = User.get_user_by_id(user),attenders = Activity.get_all_attendees(data))


### ATTEND ACTIVITY ROUTE WITH HOMEPAGE RETURN
@app.route('/getoutside/activity/<int:id>/join')
def attend_activity_return_to_home_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'activity_id' : id,
        'user_id' : session['user_id']
    }
    Activity.join_activity(data)
    return redirect("/getoutside")


### ATTEND ACTIVITY ROUTE WITH ATHLETE DASH RETURN
@app.route('/getoutside/activity/<int:id>/join2')
def attend_activity_return_to_activity_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'activity_id' : id,
        'user_id' : session['user_id']
    }
    Activity.join_activity(data)
    return redirect(f"/getoutside/activity/{id}")


### UNATTEND ACTIVITY RETURN TO HOME PAGE
@app.route('/getoutside/activity/<int:id>/unjoin')
def unattend_activity(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'activity_id' : id,
        'user_id' : session['user_id']
    }
    Activity.unjoin_activity(data)
    return redirect("/getoutside")


### DELETE ACTIVITY BY ID
@app.route('/getoutside/activity/<int:id>/delete')
def delete_activity_by_id(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id,
    }
    Activity.delete_activity_by_id(data)
    return redirect("/getoutside/athlete")
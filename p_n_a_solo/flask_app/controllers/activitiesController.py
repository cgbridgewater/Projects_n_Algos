from pprint import pprint
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.users import User
from flask_app.models.activities import Activity


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
def save_activity():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    if not Activity.validate_activity(request.form):
        return redirect('/getoutside/activities/new')  #redirect to where the form is rendered if validation fails
    Activity.save_activity(request.form) # else save form
    return redirect("/getoutside/athlete") 


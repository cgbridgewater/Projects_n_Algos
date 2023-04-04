from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.users import User


### ROUTE FOR FRIENDS PAGE 
@app.route('/dashboard/friends')
def all_users():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_friends.html", friends = User.get_friends(data),user = User.get_user_by_id(data)) ### This should be a joined list and all friends by id


from flask_app import app
from flask import render_template, request, redirect, session, flash, url_for
from flask_app.models.users import User
from flask_app.models.activities import Activity



### ROUTE FOR ATHLETE DASHBOARD -- READ BY USER_ID  (WORKING)
@app.route('/getoutside/athlete')
def user_dashboard():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    # image_file = url_for('static', filename='profile_pics/' + user.image_file)
    data ={
        'id': session['user_id']
    }
    return render_template("user_dashboard.html", user = User.get_user_by_id(data), image_file = url_for('static', filename='images/profile_pics/' + User.get_user_by_id(data).image_file),activities = Activity.all_activities(), joined = Activity.all_activities_joined(data), followers = User.all_followers(data))


### ROUTE TO DELETE ATHLETE PROFILE
@app.route('/getoutside/athlete/delete')
def delete_user_route():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    User.delete_user(data)
    return redirect('/logout') 


    ### ROUTE TO EDIT ATHLETE FORM BY ID 
@app.route('/getoutside/athlete/update')
def edit_user_form():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_update.html", user = User.get_user_by_id(data))


### ATHLETE UPDATE POST ACTION
@app.route("/getoutside/athlete/editing", methods =['POST'])
def update_user_form_action():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : session['user_id'],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
        }
    if not User.update_validation(data):
        return redirect('/getoutside/athlete/update')
    User.update_user_by_id(data)
    return redirect("/getoutside/athlete") 


    ### ROUTE TO VIEW ATHLETE BY ID
@app.route('/getoutside/athlete/<int:id>')
def show_one_user_page(id):
    data = {
    "id" : id
    }
    return render_template("user_one_view.html",  user = User.get_user_by_id(data),activities = Activity.all_activities(), joined = Activity.all_activities_joined(data))



## ROUTE FOR FRIENDS SEARCH JS FORM
@app.route('/getoutside/friends')
def friend_search_page():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("friends_search.html", allusers = User.get_all_users_without_logged_in_user(data)) 


### FRIEND / JOIN
@app.route('/getoutside/athlete/<int:id>/follow')
def follow_user_return_to_homepage(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'friend_id' : id,
        'user_id' : session['user_id']
    }
    User.follow_user(data)
    return redirect("/getoutside/athlete")


### UNFRIEND / UNJOIN
@app.route('/getoutside/athlete/<int:id>/unfollow')
def unfollow_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'friend_id' : id,
        'user_id' : session['user_id']
    }
    User.unfollow_user(data)
    return redirect("/getoutside")








############################################## CUT LINE ############################################################

# ## ROUTE FOR FRIENDS SEARCH FORM WORKING
# @app.route('/getoutside/friends')
# def friend_search_page():
#     if 'user_id' not in session:
#         msg = "you must be logged in!"
#         return redirect('/logout')
#     data ={
#         'id': session['user_id']
#     }
#     return render_template("friends_find.html",user = User.get_user_by_id(data)) 


# ## ROUTE FOR FRIENDS SEARCH ACTION PAGE   TESTING
# @app.route('/getoutside/friends/search', methods = ['POST'])
# def friend_search_action():
#     if 'user_id' not in session:
#         msg = "you must be logged in!"
#         return redirect('/logout')
#     data = {
#         "id" : session['user_id'],
#         "first_name" :  request.form['first_name'],
#         "last_name" : request.form['first_name']
#         }
#     if not User.search_validation(data):
#         return redirect ('/getoutside/friends')
#     user = User.find_friends_by_name(data)
#     return redirect("friends_result.html" ) 





# ### UPLOAD IMAGE ROUTE
# @app.route("/getoutside/addimage", methods=['POST'])
# def upload_image():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         'id': session['user_id']
#     }
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect('/getoutside/athlete/update')
#     file = request.files['file']
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect('/getoutside/athlete/update')
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         #print('upload_image filename: ' + filename)
#         flash('Image successfully uploaded and displayed below')
#         return render_template("user_update.html", user = User.get_user_by_id(data), filename = filename)
#     else:
#         flash('Allowed image types are - png, jpg, jpeg, gif')
#         return redirect('/getoutside/athlete/update')

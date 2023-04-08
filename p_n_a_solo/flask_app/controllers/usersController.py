from flask_app import app
from flask import render_template, request, redirect, session, flash, url_for
from flask_app.models.users import User
from flask_app.models.activities import Activity


### ROUTE FOR HOME PAGE  (WORKING)
@app.route('/getoutside')
def home_page():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template(
        "dashboard.html", user = User.get_user_by_id(data), activities = Activity.all_activities_with_joined_activities(data))
        # activities = Activity.all_activities(), 
        # joined = Activity.all_joined()


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
    return render_template("user_dashboard.html", user = User.get_user_by_id(data), image_file = url_for('static', filename='images/profile_pics/' + User.get_user_by_id(data).image_file),activities = Activity.all_activities(), joined = Activity.all_activities_joined(data))


### ROUTE TO DELETE USER BY USER_ID (WORKING)
@app.route('/getoutside/delete')
def delete_user_route():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    User.delete_user(data)
    return redirect('/logout') 


    ### ROUTE TO EDIT USER FORM BY USER_ID (WORKING)
@app.route('/getoutside/athlete/update')
def edit_user_form():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_update.html", user = User.get_user_by_id(data))


### ROUTE TO PROCESS USER UPDATE FORM (WORKING)
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
    if not User.validate_update(data):
        return redirect('/getoutside/athlete/update')
    User.update_user_by_id(data)
    return redirect("/getoutside/athlete") 


    ### ROUTE TO VIEW USER PROFILE PAGE BY "ID" TESTING
@app.route('/getoutside/athlete/<int:id>')
def show_one_user_page(id):
    data = {
    "id" : id
    }
    return render_template("user_oneview.html",  user = User.get_user_by_id(data), image_file = url_for('static', filename='images/profile_pics/' + User.get_user_by_id(data).image_file),activities = Activity.all_activities(), joined = Activity.all_activities_joined(data))


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







### delete below this line when ready!

#######  EXAMPLE ROUTES

# ### ROUTE TO CREATE NEW USER AND DIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (WORKING)
# @app.route("/users/creating" , methods=['POST'])
# def addUser():
#     new_user_id = User.save(request.form)
#     return redirect(f'/users/read/{new_user_id}')





    

from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users import User

#file upload




### ROUTE FOR HOME PAGE -- READ BY USER_ID  (WORKING)
@app.route('/getoutside')
def home():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html", user = User.get_user_by_id(data))


### ROUTE FOR USER DASHBOARD -- READ BY USER_ID  (WORKING)
@app.route('/getoutside/athlete')
def dashboard():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_dashboard.html", user = User.get_user_by_id(data))





### ROUTE TO DELETE USER BY USER_ID (WORKING)
@app.route('/getoutside/delete')
def delete_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    User.delete_user(data)
    return redirect('/logout') 




    ### ROUTE TO EDIT USER FORM BY USER_ID (WORKING)
@app.route('/getoutside/athlete/update')
def edit_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_update.html", user = User.get_user_by_id(data))




### ROUTE TO PROCESS USER UPDATE FORM (WORKING)
@app.route("/getoutside/athlete/editing", methods =['POST'])
def update_user():
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



#     ### ROUTE TO VIEW USER PROFILE PAGE BY "ID" (WORKING)
# @app.route('/users/read/<int:id>')
# def show_one_user(id):
#     data = {
#     "id" : id
#     }
#     return render_template("read(one).html", user = User.get_one_user(data))




    

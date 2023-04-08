from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


### HOME ROUTE
@app.route('/')
def index():
    return redirect("/getoutside/login")


### LOGIN ROUTE
@app.route('/getoutside/login')
def login_page():
    return render_template("login.html")


### LOGIN ROUTE
@app.route('/getoutside/register')
def register_page():
    return render_template("register.html")


### ROUTE FOR REGISTRATION
@app.route('/register', methods= ['POST'])
def register():
    # We call the staticmethod on User model to validate
    if not User.registration_validations(request.form):
        session["first_name"] = request.form["first_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["last_name"] = request.form["last_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["email"] = request.form["email"] ### HOLDING FORM DATA FOR RESUBMIT
        return redirect('/getoutside/register')# redirect to the route where the user form is rendered if there are errors:
    pw_hash = bcrypt.generate_password_hash(request.form['password'])    ### hash password once validations are passed
    print(pw_hash) 
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.create(data) ### save user
    session.pop("first_name", None)  ### clear form place holder sessions
    session.pop("last_name", None)   ### clear form place holder sessions
    session.pop("email", None)       ### clear form place holder sessions
    session['user_id'] = user_id     ### start user id session to prove logged in
    return redirect("/getoutside")    ### go to dashboard if no validation errors


### ROUTE FOR LOGIN
@app.route('/login', methods= ['POST'])
def login():
    # We call the staticmethod on User model to validate
    session["email2"] = request.form["email"] ### HOLDING FORM DATA FOR RESUBMIT
    data = { "email" : request.form["email"] } ###data list for checking email
    user_in_db = User.check_for_email_exists(data) ###email exists in db check
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/getoutside/login")  ### redirect if fails
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']): ###check hashed pw
        flash("Invalid Email/Password", "login")
        return redirect("/getoutside/login") ### redirect if fails
    if not User.login_validation(request.form):
    # if there are errors:
        return redirect('/getoutside/login') # redirect to the route where the user form is rendered.
    session["user_id"] = user_in_db.id   ### create session to test logged in
    session.pop("email2", None)    ### pop log in session
    return redirect("/getoutside")   ### else no validation errors:


### ROUTE FOR LOGOUT 
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/getoutside/login")


### CATCH ALL DINO GAME  (WORKING)
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("catch_all_dinosaur.html")
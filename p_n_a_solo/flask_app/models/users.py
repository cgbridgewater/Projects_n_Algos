from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


### USER CLASS
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.image_file = data['image_file']
        self.email = data['email']    
        self.password = data['password']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.joined = []NOT IN USE?
        # self.joiners = []NOT IN USE?
        # self.joinerIds = []NOT IN USE?
        # self.activities = []    NOT IN USE?


### REGISTRATION VALIDATIONS (WORKING)
    @staticmethod
    def registration_validations(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3: ### first name length check
            flash("First Name must be at least 3 characters.", "register")
            is_valid = False
        if len(user['last_name']) < 3: ### last name length check
            flash("Last Name must be at least 3 characters.", "register")
            is_valid = False
        if len(user['password']) < 3: ### password length check
            flash("Password must be a valid password.", "register")
            is_valid = False
        if len(user['confirm_password']) < 4: ### password length check
            flash("Password must be a valid password.", "register")
            is_valid = False
        if user['password'] != user['confirm_password']: #### passwords must match
            flash("Passwords must match!!", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):  ### checks email formating
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['email']) < 3:    ### email length check
            flash("Email must be a valid email.", "register")
            is_valid = False
        if User.email_exists(user):  ### check user email is origional
            flash("This email is already taken!", "register")
            is_valid = False 
        return is_valid ### if you make it this far, is good to go!


### LOGIN VALIDATIONS WORKING
    @staticmethod
    def login_validation(user):
        is_valid = True # we assume this is true
        if len(user['email']) < 3:    ### email length check
            flash("Email must be a valid email.", "login")
            is_valid = False
        if len(user['password']) < 3: ### password length check
            flash("Password must be a valid password.", "login")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


### UPDATE VALIDATIONS (WORKING)
    @staticmethod
    def update_validation(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3: ### password length check
            flash("First name must be at least 3 charactors long.", "update")
            is_valid = False
        if len(user['last_name']) < 3: ### password length check
            flash("Last name must be at least 3 charactors long.", "update")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):  ### checks email formating
            flash("Invalid email address!", "update")
            is_valid = False
        # if User.email_exists(user):  ### check user email is origional
        #     flash("This email is already taken!", "update")
        #     is_valid = False 
        return is_valid ### if you make it this far, is good to go!


### CHECK FOR EXISTING EMAIL (WORKING)
    @classmethod 
    def check_for_email_exists(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("test_app").query_db(query,data)
        if len(result) < 1:
            return False   #didn't find a matching user
        return cls(result[0])

### Search VALIDATIONS TESTING
    @staticmethod
    def search_validation(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2: ### password length check
            flash("First name must be at least 2 charactors long.", "update")
            is_valid = False
        if len(user['last_name']) < 2: ### password length check
            flash("Last name must be at least 2 charactors long.", "update")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!




### CREATE AND SAVE NEW USER (WORKING)
    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL('test_app').query_db(query,data)


### GET USER BY ID (WORKING)
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('test_app').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### DELETE USER BY ID (WORKING)
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('test_app').query_db(query,data) 


### UPDATE USER BY ID (WORKING)
    @classmethod
    def update_user_by_id(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('test_app').query_db(query,data)



### FIND FRIENDS SEARCH                 (NOT IN USE YET)
    @classmethod
    def find_friends_by_name(cls,data):
        query = """SELECT * FROM users 
            WHERE first_name LIKE  "%(first_name)s"
            OR last_name LIKE "%(last_name)s%" AND id <> %(id)s;"""
        results = connectToMySQL('test_app').query_db(query,data)
        print(results)
        users = []
        for i in results:
            users.append(cls(i))
        return users

# use this query to search by partial and filter out user id

	# SELECT * FROM users WHERE first_name LIKE "% %" 
	# 		and last_name Like "% %" and id <> 3;


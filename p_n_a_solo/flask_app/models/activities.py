from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users
from flask import flash, session
import datetime
from pprint import pprint



### ACTIVITY CLASS
class Activity:
    def __init__(self,data):
        self.id = data['id']
        self.activity = data['activity']
        self.location = data['location']
        self.date = data['date']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.activities = []


### Activity FORM VALIDATIONS
    @staticmethod
    def validate_activity(activity):
        is_valid = True # we assume this is true
        try:
            datetime.datetime.strptime(activity['date'], '%Y-%m-%d')
        except ValueError:
            flash("A date must be provided.", "activity")
            is_valid = False    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        if len(activity['location']) < 3: ### length check
            flash("Location must be at least 3 charactors", "activity")
            is_valid = False
        if len(activity['activity']) < 1: ### activity check
            flash("Please select an activity", "activity")
            is_valid = False

        return is_valid ### if you make it this far, is good to go!



    ### Save activity WORKING
    @classmethod
    def save_activity(clas,data):
        query = """
            INSERT INTO activities (user_id, activity, location, date)
            VALUES ( %(user_id)s, %(activity)s, %(location)s, %(date)s )
        """
        return connectToMySQL('test_app').query_db(query,data)




    ###Get activity by id                     (testing)
    @classmethod
    def get_one_activity(cls,data):
        query = """
            SELECT * FROM activities WHERE id = %(id)s;
        """
        result = connectToMySQL('test_app').query_db(query,data)
        print(result)
        if len(result) == 0: #if no activities found, return an empty list
            return None
        else: # if at least one activity is found
            return cls(result[0])

    ### UPDATE activity BY ID                        (testing)
    @classmethod
    def update_activity(cls,data):
        query = """
            UPDATE activities SET activity = %(activity)s , location = %(location)s , date = %(date)s WHERE id = %(id)s;
        """
        return connectToMySQL('test_app').query_db(query,data)


    ### DELETE activity BY ID                            (testing)
    @classmethod
    def delete_activity(cls,data):
        query = """
            DELETE FROM activities WHERE id = %(id)s;
        """
        return connectToMySQL('test_app').query_db(query,data) 


    
    
    
    
    ### READ ONE ACTIVITY + CREATOR             testing!!!
    @classmethod
    def one_activity_and_user(cls,data):
        query = """
            SELECT activities.id, activities.created_at, activities.updated_at, activity, location, date,
            users.id as user_id, first_name, last_name, email,password, image_file, users.created_at as uc, users.updated_at as uu FROM activities
            JOIN users ON activities.user_id = users.id
            WHERE activities.id = %(id)s
            ORDER BY date ASC;
        """
        results = connectToMySQL('test_app').query_db(query,data)
        pprint(results)
        one_activity = cls(results[0])# Prepare to make a User class instance, looking at the class in models/user.py
        one_activity.creator = users.User({# Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": results[0]['user_id'],
                "first_name": results[0]['first_name'],
                "last_name": results[0]['last_name'],
                "email": results[0]['email'],
                "image_file": result[0]['image_file'],
                "password": results[0]['password'],
                "created_at": results[0]['uc'],
                "updated_at": results[0]['uu'],
        })
        return one_activity



    ### READ ALL ACTIVITIES + USER                         TESTING!!!
    @classmethod
    def all_activities(cls): #get all activities and the creator
        query = """
            SELECT activities.id, activities.created_at, activities.updated_at, activity, location, date, 
            users.id as user_id, first_name, last_name, email, password, image_file, users.created_at as uc, users.updated_at as uu
            FROM activities
            JOIN users on users.id = activities.user_id
            ORDER BY date ASC;
        """
        results = connectToMySQL('test_app').query_db(query)
        pprint(results)
        all_activities = [] # empty array to fill with each activity
        for row in results:# Create a Activity class instance from the information from each db row
            one_activity = cls(row)
            one_activity.creator = users.User({
                "id": row['user_id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "image_file": row['image_file'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['uc'],
                "updated_at": row['uu'],
            })
            all_activities.append(one_activity)### Append the activity and creator to the array
        return all_activities



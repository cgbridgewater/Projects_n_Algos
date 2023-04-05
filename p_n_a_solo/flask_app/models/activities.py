from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users
from flask import flash, session
import datetime



### ACTIVITY CLASS
class Activity:
    def __init__(self,data):
        self.id = data['id']
        self.what = data['what']
        self.where = data['where']
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



    @classmethod
    def save_activity(clas,data):
        query = '''
        INSERT INTO activities (user_id, activity, location, date)
        VALUES ( %(user_id)s, %(activity)s, %(location)s, %(date)s )
        '''
        return connectToMySQL('test_app').query_db(query,data)




    ###Get activity by id (testing)
    @classmethod
    def get_one_activity(cls,data):
        query = '''
        SELECT * FROM activities WHERE id = %(id)s;
        '''
        result = connectToMySQL('test_app').query_db(query,data)
        print(result)
        if len(result) == 0: #if no activities found, return an empty list
            return None
        else: # if at least one activity is found
            return cls(result[0])

    ### UPDATE activity BY ID (testing)
    @classmethod
    def update_activity(cls,data):
        query = '''
        UPDATE activities SET what = %(what)s , where = %(where)s , date = %(date)s WHERE id = %(id)s;
        '''
        return connectToMySQL('test_app').query_db(query,data)


    ### DELETE activity BY ID (testing)
    @classmethod
    def delete_activity(cls,data):
        query = '''
        DELETE FROM activities WHERE id = %(id)s;
        '''
        return connectToMySQL('test_app').query_db(query,data) 
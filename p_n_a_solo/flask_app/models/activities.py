from flask_app.config.mysqlconnection import connectToMySQL



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
            datetime.datetime.strptime(order['date'], '%Y-%m-%d')
        except ValueError:
            flash("A date must be provided.")
        if len(activity['where']) < 3: ### length check
            flash("Last Name must be at least 3 characters.", "register")
            is_valid = False
        if len(activity['date']) < 3: ### date check
            flash("Password must be a valid password.", "register")
            is_valid = False

        return is_valid ### if you make it this far, is good to go!


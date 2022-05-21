from flask import flash
#from flask_app.config.mysqlconnection import connectToMySQL


# email address validations
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')


# Note to group - unable to view the .bmpr file with the wireframe so I couldn't do this part
class User:
    db_name = ""

    def __init__(self, data):
        # will need to do self.__ = data['__']
        pass

    @staticmethod
    def validate_user(user):
        is_valid = True
        # Will need a lot more validations here but here is the email validation
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "create_user")
            is_valid = False
        return is_valid

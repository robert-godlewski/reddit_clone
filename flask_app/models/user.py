from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask import session

# from flask_app.models import favorite


# email address validations
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')


# Note to group - unable to view the .bmpr file with the wireframe so I couldn't do this part
class User:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.userName = data['userName']
        self.email = data['email']
        self.password = data['password']
        self.favorites = []



    @classmethod
    def registerUser( cls,data ):
        query = "INSERT INTO users (userName, email, password) VALUES (%(userName)s,%(email)s, %(password)s);"
        return connectToMySQL('redditClone').query_db( query, data )

    @classmethod
    def userByEmail(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('redditClone').query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validation_registrationForm(user): #confirms form matches requirements
        is_valid = True
        # Will need a lot more validations here but here is the email validation
        if not EMAIL_REGEX.match(user['email']) or not User.validation_EmailExistsInDB(user['email']): 
            flash("Invalid email address", "create_user")
            is_valid = False
        return is_valid

    @staticmethod
    def validation_EmailExistsInDB(data): #checks that email exists in database
        query = "SELECT email FROM users"
        results = connectToMySQL('redditClone').query_db(query)
        for users in results:
            if data['email'] == users['email']:
                return False
        return True



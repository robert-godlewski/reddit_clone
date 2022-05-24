from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# Why do we need to import session in the models?
from flask import session

# There is no favorite model?
#from flask_app.models import favorite


# email address validations
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')


# We should probably vote on camelCase vs snake_case? for consistency and easier to debug if needed and also apply it to the Database if we need/want to.
class User:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.userName = data['userName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.posts = []
        self.comments = []
        # What is the point of favorites? or should this actually be groups?
        self.favorites = []

    @classmethod
    def registerUser(cls, data):
        # Needed to add in all of the variables
        query = '''
        INSERT INTO users ( userName, email, password, createdAt, updatedAt) 
        VALUES (%(userName)s, %(email)s, %(password)s, NOW(), NOW() );
        '''
        # Note to group - The purpose of having db_name variable is to decrease the amount of times we need to type it out in the class and to remove possiblity of a bug
        # original - return connectToMySQL('redditClone').query_db(query, data)
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def userByEmail(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @staticmethod
    # confirms form matches requirements
    def validation_registrationForm(user):
        is_valid = True
        # How long do you guys think about the lenghts for userName and password?
        if len(user['userName']) < 3:
            flash("User name needs to be at least 3 characters long", "create_user")
            is_valid = False
        #original - if not EMAIL_REGEX.match(user['email']) or not User.validation_EmailExistsInDB(user['email']):
        if not EMAIL_REGEX.match(user['email']) or not User.userByEmail(user):
            flash("Invalid email address", "create_user")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password needs to be at least 8 characters long", "create_user")
            is_valid = False
        return is_valid

    @staticmethod
    # checks that email exists in database
    # This is actually redundant and slow because of the for loop can just use the userByEmail to find an email for the validation.
    # userByEmail will either return the email in question or False.
    def validation_EmailExistsInDB(data):
        query = "SELECT email FROM users"
        results = connectToMySQL('redditClone').query_db(query)
        for users in results:
            if data['email'] == users['email']:
                return False
        return True

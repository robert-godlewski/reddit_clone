from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


# email address validations
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')


class User:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []
        self.comments = []

    @classmethod
    def register_user(cls, data):
        query = '''
        INSERT INTO users ( user_name, email, password, created_at, updated_at) 
        VALUES (%(userName)s, %(email)s, %(password)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validation_registration_form(user):
        is_valid = True
        if len(user['userName']) < 3:
            flash("User name needs to be at least 3 characters long", "create_user")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']) or not User.userByEmail(user):
            flash("Invalid email address", "create_user")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password needs to be at least 8 characters long", "create_user")
            is_valid = False
        return is_valid

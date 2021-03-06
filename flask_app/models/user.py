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
        INSERT INTO user ( user_name, email, password, created_at, updated_at) 
        VALUES (%(user_name)s, %(email)s, %(password)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def user_by_email(cls, data):
        print(f'In data: {data}')
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(f'Gathered results: {results}')
        if len(results) >= 1: 
            return cls(results[0])
        else:
            return False

    @classmethod
    def user_by_id(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['user_name']) < 3:
            flash("User name needs to be at least 3 characters long", "create_user")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "create_user")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password needs to be at least 8 characters long", "create_user")
            is_valid = False
        if user['conf_password'] != user['password']:
            flash("Passwords do not match", "create_user")
            is_valid = False
        return is_valid

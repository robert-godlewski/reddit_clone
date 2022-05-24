from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


# Some of the variables and queries are not consistent with the db!
# We need to vote on camelCase vs. snake_case
class Post:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.likeCount = data['likeCount']
        self.content = data['content']
        self.user_id = data['user_id']
        self.group_id = data['group_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def savePost(cls, data):
        # This query will cause problems with the db - variable names are not consistent
        query = '''
        INSERT INTO post( title, likeCount, content, user_id, group_id, created_at, updated_at) 
        VALUES (%(title)s, 0, %(content)s, %(user_id)s, %(group_id)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def updatePost(cls, data):
        # This query will cause problems with the db - variable names are not consistent
        query = '''
        UPDATE post 
        SET title = %(title)s, content=%(content)s, updated_at = NOW() 
        WHERE id = %(id)s;
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def deletePost(cls, data):
        query = "DELETE FROM post WHERE id = %(id)s;"
        return connectToMySQL("redditClone").query_db(query, data)

    @classmethod
    def showOnePost(cls, data):
        query = "SELECT * FROM post WHERE id = %(id)s;"
        result = connectToMySQL("redditClone").query_db(query, data)
        return cls(result[0])

    @classmethod
    def getAllPosts(cls):
        # Question: Should we have an ascending/descending order to organize the data based off of when it's updated at?
        # Proposed query => query = "SELECT * FROM group ORDER BY updatedAt ASC (or) DESC;"
        query = "SELECT * FROM post;"
        result = connectToMySQL("redditClone").query_db(query)
        all_posts = []
        for row in result:
            all_posts.append(cls(row))
        return all_posts

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['title']) < 1 or len(post['content']) < 1:
            is_valid = False
            flash("Post must not be empty!", 'post')
        return is_valid

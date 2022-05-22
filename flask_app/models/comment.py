from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Comment:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.likeCount = data['likeCount']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def create_comment(cls, data):
        query = '''
        INSERT INTO comment (content, likeCount, user_id, post_id, createdAt, updatedAt) 
        VALUES (%(content)s, 0, %(user_id)s, %(post_id)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_comments_by_post(cls, data):
        query = "SELECT * FROM comment WHERE post_id = %(post_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        all_commets = list()
        for row in results:
            commet = cls(row)
            all_commets.append(commet)
        return all_commets

    @classmethod
    def get_comment_by_id(cls, data):
        query = "SELECT * FROM comment WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_comment_like(cls, data):  # conditional for upvote downvote here?
        query = "UPDATE comment SET likeCount = %(likeCount)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Post:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.group_id = data['group_id']
        self.title = data['title']
        self.content = data['content']
        self.like_count = data['like_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_post(cls, data):
        query = '''
        INSERT INTO post (title, content, like_count, user_id, created_at, updated_at)
        VALUES (%(title)s, %(content)s, 0, %(user_id)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_post(cls, data):
        query = '''
        UPDATE post
        SET title = %(title)s, content=%(content)s, updated_at = NOW()
        WHERE id = %(id)s;
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_post(cls, data):
        query = "DELETE FROM post WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def focus_post(cls, data):
        query = "SELECT post.title as title, post.content as post, post.user_id as post_user_id, post.id as id, post.group_id as group_id, post.like_count as post_like_count, post.created_at as post_created_At, post.updated_at as post_updated_at, comment.content as comment, comment.like_count as comment_like_count, comment.created_at as comment_created_at, comment.updated_at as comment_updated_at, user.id as user_id, user.user_name as user_name FROM Post LEFT Join comment on post.id = comment.post_id left join user on comment.user_id = user.id where post.id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        all_posts = []
        for row in result:
            all_posts.append(row)
        return all_posts

    @ classmethod
    def show_one_post(cls, data):
        query = "SELECT * FROM post WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        print(result)

    @ classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM post ORDER BY updated_at DESC;"
        result = connectToMySQL(cls.db_name).query_db(query)
        all_posts = []
        for row in result:
            all_posts.append(cls(row))
        # print('All of the posts colected from db:')
        # print(all_posts)
        return all_posts

    @ staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['title']) < 1 or len(post['content']) < 1:
            is_valid = False
            flash("Post must not be empty!", 'post')
        return is_valid

from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL




class Group:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']


    @classmethod
    def create_group(cls, data):
        query = '''
        INSERT INTO group (name, createdAt, updatedAt) 
        VALUES (%(name)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_group_by_id(cls, data):
        query = "SELECT * FROM comment WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])
 
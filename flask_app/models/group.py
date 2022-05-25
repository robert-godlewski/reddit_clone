#from flask import flash - Needed for validations
from flask_app.config.mysqlconnection import connectToMySQL


class Group:
    db_name = "redditClone"

    def __init__(self, data):
        self.id = data['id']
        self.group_name = data['group_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_group(cls, data):
        query = '''
        INSERT INTO group (group_name, created_at, updated_at) 
        VALUES (%(name)s, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_group_by_id(cls, data):
        query = "SELECT * FROM group WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM group WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def update (cls, data):
        query = "SELECT * FROM group WHERE id = %(id)s;"
        results =connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM group;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_group = []
        for row in results:
            all_group.append( cls(row) )
        return all_group

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import items

class Friendship:
  db_name = 'python-exam-practice'

  def __init__(self, data):
    self.id = data['id']
    self.user_id = data['user_id']
    self.friend_id = data['friend_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO friendships (user_id, friend_id) VALUES ( %(user_id)s , %(friend_id)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def check(cls, data):
    query = 'SELECT id FROM friendships WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    if len(results) > 0:
      return True
    return False

  # @classmethod
  # def get_one(cls, data):
  #   query = "SELECT * FROM friendships WHERE id = %(id)s;"
  #   result = connectToMySQL(cls.db_name).query_db(query, data)
  #   if len(result) < 1:
  #     return None
  #   return cls(result[0])

  # @classmethod
  # def get_all(cls):
  #   query = 'SELECT * FROM friendships;'
  #   return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  # @classmethod
  # def update(cls, data):
  #   query = "UPDATE friendships SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)

  # @classmethod
  # def destroy(cls, data):
  #   query = "DELETE FROM friendships WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)
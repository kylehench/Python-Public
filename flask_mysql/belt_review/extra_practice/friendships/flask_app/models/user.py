from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
  db_name = 'python-exam-practice'

  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.friend = None

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO users (first_name, last_name) VALUES ( %(first_name)s , %(last_name)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  # @classmethod
  # def get_one(cls, data):
  #   query = "SELECT * FROM users WHERE id = %(id)s;"
  #   result = connectToMySQL(cls.db_name).query_db(query, data)
  #   if len(result) < 1:
  #     return None
  #   return cls(result[0])

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM users;'
    return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  @classmethod
  def get_all_with_friends(cls):
    query = 'SELECT * FROM users JOIN friendships ON users.id = friendships.user_id JOIN users AS user2 ON friendships.friend_id = user2.id;'
    results = connectToMySQL(cls.db_name).query_db(query)
    users = []
    for row in results:
      user = cls(row)
      friend_data = {
        'id' : row['user2.id'],
        'first_name' : row['user2.first_name'],
        'last_name' : row['user2.last_name'],
        'created_at' : row['user2.created_at'],
        'updated_at' : row['user2.updated_at']
      }
      user.friend = cls(friend_data)
      users.append(user)
    return users

  # @classmethod
  # def update(cls, data):
  #   query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)

  # @classmethod
  # def destroy(cls, data):
  #   query = "DELETE FROM users WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)
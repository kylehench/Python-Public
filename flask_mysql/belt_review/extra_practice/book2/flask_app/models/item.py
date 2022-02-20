from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import items

class Item:
  db_name = ''

  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO items (first_name, last_name, email, password) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM items WHERE id = %(id)s;"
    result = connectToMySQL(cls.db_name).query_db(query, data)
    if len(result) < 1:
      return None
    return cls(result[0])

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM items;'
    return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  @classmethod
  def update(cls, data):
    query = "UPDATE items SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM items WHERE id = %(id)s ;"
    return connectToMySQL(cls.db_name).query_db(query, data)
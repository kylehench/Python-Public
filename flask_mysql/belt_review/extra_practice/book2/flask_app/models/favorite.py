from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import items

class Favorite:
  db_name = 'python-exam-practice'

  def __init__(self, data):
    self.id = data['id']
    self.author_id = data['author_id']
    self.book_id = data['book_id']

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO favorites (author_id, book_id) VALUES ( %(author_id)s , %(book_id)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  # @classmethod
  # def get_one(cls, data):
  #   query = "SELECT * FROM books WHERE id = %(id)s;"
  #   result = connectToMySQL(cls.db_name).query_db(query, data)
  #   if len(result) < 1:
  #     return None
  #   return cls(result[0])

  # @classmethod
  # def get_all(cls):
  #   query = 'SELECT * FROM books;'
  #   return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  # @classmethod
  # def update(cls, data):
  #   query = "UPDATE books SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)

  # @classmethod
  # def destroy(cls, data):
  #   query = "DELETE FROM books WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)
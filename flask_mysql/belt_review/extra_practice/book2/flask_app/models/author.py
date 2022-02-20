from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import book

class Author:
  db_name = 'python-exam-practice'

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.books = []

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO authors (name) VALUES ( %(name)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM authors WHERE id = %(id)s;"
    result = connectToMySQL(cls.db_name).query_db(query, data)
    if len(result) < 1:
      return None
    return cls(result[0])

  @classmethod
  def get_one_with_books(cls, data):
    query = 'SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    author = cls(results[0])
    for row in results:
      if row['books.id'] == None:
        break
      book_data = {
        'id' : row['books.id'],
        'created_at' : row['books.created_at'],
        'updated_at' : row['books.updated_at'],
        'title' : row['title'],
        'num_of_pages' : row['num_of_pages'],
      }
      author.books.append(book.Book(book_data))
    return author

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM authors;'
    return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  @classmethod
  def get_unfavs(cls, data):
    query = 'SELECT * FROM authors WHERE id NOT IN (SELECT author_id FROM favorites WHERE book_id=  %(book_id)s );'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    unfavs = []
    for row in results:
      unfavs.append(cls(row))
    return unfavs

  # @classmethod
  # def update(cls, data):
  #   query = "UPDATE authors SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM authors WHERE id = %(id)s ;"
    return connectToMySQL(cls.db_name).query_db(query, data)
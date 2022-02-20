from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import author

class Book:
  db_name = 'python-exam-practice'

  def __init__(self, data):
    self.id = data['id']
    self.title = data['title']
    self.num_of_pages = data['num_of_pages']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.authors = []

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO books (title, num_of_pages) VALUES ( %(title)s , %(num_of_pages)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM books WHERE id = %(id)s;"
    result = connectToMySQL(cls.db_name).query_db(query, data)
    if len(result) < 1:
      return None
    return cls(result[0])

  @classmethod
  def get_one_with_authors(cls, data):
    query = 'SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    book = cls(results[0])
    for row in results:
      if row['authors.id'] == None:
        break
      author_data = {
        'id' : row['authors.id'],
        'created_at' : row['authors.created_at'],
        'updated_at' : row['authors.updated_at'],
        'name' : row['name'],
      }
      book.authors.append(author.Author(author_data))
    return book

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM books;'
    return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  @classmethod
  def get_unfavs(cls, data):
    query = 'SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM favorites WHERE author_id=  %(author_id)s );'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    unfavs = []
    for row in results:
      unfavs.append(cls(row))
    return unfavs

  # @classmethod
  # def update(cls, data):
  #   query = "UPDATE books SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
  #   return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM books WHERE id = %(id)s ;"
    return connectToMySQL(cls.db_name).query_db(query, data)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
  db_name = 'books_schema'
  
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.fav_books = []

  # @classmethod
  # def add_author(cls, data):
  #   query = 'INSERT INTO authors (name) VALUES ( %(name)s );'
  #   return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO authors (name) VALUES ( %(name)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  # @classmethod
  # def get_all(cls):
  #   query = 'SELECT * FROM authors;'
  #   return connectToMySQL(cls.db_name).query_db(query)

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM authors;'
    results = connectToMySQL(cls.db_name).query_db(query)
    all_authors = []
    for row in results:
      all_authors.append(cls(row))
    return all_authors

  @classmethod
  def get_one_with_books(cls, data):
    query = 'SELECT * FROM authors\
      LEFT JOIN favorites ON authors.id = favorites.author_id\
      LEFT JOIN books ON favorites.book_id = books.id\
      WHERE authors.id = %(id)s \
      GROUP BY books.id;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    one_author = cls(results[0])
    for row in results:
      if row['books.id']==None:
        break
      book_data = {
        'id' : row['books.id'],
        'title' : row['title'],
        'created_at' : row['books.created_at'],
        'updated_at' : row['books.updated_at'],
        'num_of_pages' : row['num_of_pages']
      }
      one_author.fav_books.append(book.Book(book_data))
    return one_author

  # @classmethod
  # def unfav_books(cls, data):
  #   query = 'SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s );'
  #   results = connectToMySQL(cls.db_name).query_db(query, data)
  #   unfav_books = []
  #   for row in results:
  #     unfav_books.append(cls(row))
  #   return unfav_books
  @classmethod
  def unfav_authors(cls, data):
    query = 'SELECT * from authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s );'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    unfav_authors = []
    for row in results:
      unfav_authors.append(cls(row))
    return unfav_authors
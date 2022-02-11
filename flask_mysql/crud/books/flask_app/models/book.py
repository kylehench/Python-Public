from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
  db_name = 'books_schema'

  def __init__(self, data):
    self.id = data['id']
    self.title = data['title']
    self.num_of_pages = data['num_of_pages']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.fav_authors = []

  @classmethod
  def add_book(cls, data):
    query = 'INSERT INTO books (title, num_of_pages) VALUES ( %(title)s , %(num_of_pages)s )'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM books'
    results = connectToMySQL(cls.db_name).query_db(query)
    books = []
    for result in results:
      books.append(cls(result))
    return books

  @classmethod
  def get_one_with_authors(cls, data):
    query = 'SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    print(query, data)
    print('results:  ',results)
    book = Book(results[0])
    for row in results:
      author_data = {
        'id' : row['authors.id'],
        'name' : row['name'],
        'created_at' : row['authors.created_at'],
        'updated_at' : row['authors.updated_at']
      }
      book.fav_authors.append(author.Author(author_data))
    return book

  @classmethod
  def unfav_books(cls, data):
    query = 'SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s );'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    unfav_books = []
    for row in results:
      unfav_books.append(cls(row))
    return unfav_books

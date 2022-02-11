from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
  db_name = 'books_schema'

  def __init__(self, data):
    self.author_id = data['author_id']
    self.book_id = data['book_id']

  @classmethod
  def create_fav(cls, data):
    query = 'INSERT INTO favorites (author_id, book_id) VALUES ( %(author_id)s , %(book_id)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

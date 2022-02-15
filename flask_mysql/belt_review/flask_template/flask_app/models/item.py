from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_app.models import items

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Item:
  db_name = ''

  def __init__(self, data):
    self.id = data['id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM items;'
    results = connectToMySQL(cls.db_name).query_db(query)
    items = []
    for row in results:
      items.append(cls(row))
    return items
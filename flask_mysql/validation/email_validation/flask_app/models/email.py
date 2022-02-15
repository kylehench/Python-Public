from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_app.models import items

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
  db_name = 'emails_schema'

  def __init__(self, data):
    self.id = data['id']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @staticmethod
  def validate_email(email):
    is_valid = True
    query = 'SELECT * FROM emails WHERE email= %(email)s ;'
    if len(connectToMySQL(Email.db_name).query_db(query, email)) > 0:
      flash("Email address already taken!")
      is_valid = False
    if not EMAIL_REGEX.match(email['email']):
      flash("Invalid email address!")
      is_valid = False
    return is_valid

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO emails (email) VALUES ( %(email)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def destroy(cls, data):
    query = 'DELETE FROM emails WHERE id = %(id)s ;'
    return connectToMySQL(cls.db_name).query_db(query, data)


  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM emails'
    results = connectToMySQL(cls.db_name).query_db(query)
    emails = []
    for row in results:
      emails.append(cls(row))
    return results

  @classmethod
  def get_one(cls, data):
    query = 'SELECT * FROM emails WHERE id = %(id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    if len(results)==1:
      return cls(results[0])
    else:
      return None
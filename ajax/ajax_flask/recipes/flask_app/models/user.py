from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_app.models import items

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
  db_name = 'recipes_schema'

  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  @staticmethod
  def validate_email(data):
    messages = []
    query = 'SELECT * FROM users WHERE email= %(email)s ;'
    if len(connectToMySQL(User.db_name).query_db(query, data)) > 0:
      messages.append("Email address already taken!")
    if not EMAIL_REGEX.match(data['email']):
      messages.append("Invalid email address!")
    return messages

  @staticmethod
  def validate_user(user):
    messages = []
    if len(user['first_name'])<2:
      messages.append('First name must be at least 2 characters.')
    if len(user['last_name'])<2:
      messages.append('Last name must be at least 2 characters.')
    if not user['first_name'].isalpha():
      messages.append('First name may only contain letters.')
    if not user['last_name'].isalpha():
      messages.append('Last name may only contain letters.')
    if len(user['password'])<8:
      messages.append('Password must be at least 8 characters.')
    if user['password']!=user['password_confirm']:
      messages.append('Passwords do not match.')
    pw = user['password']
    if not all([any(char.isnumeric() for char in pw), any(char.isupper() for char in pw), any(char.islower() for char in pw)]):
      messages.append('Password requires at least 1 number, 1 uppercase, and 1 lowercase characters.')
    return messages

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_by_email(cls, data):
      query = "SELECT * FROM users WHERE email = %(email)s;"
      result = connectToMySQL(cls.db_name).query_db(query, data)
      if len(result) < 1:
          return False
      return cls(result[0])

  @classmethod
  def get_by_id(cls, data):
      query = "SELECT * FROM users WHERE id = %(id)s;"
      result = connectToMySQL(cls.db_name).query_db(query, data)
      if len(result) < 1:
          return False
      return cls(result[0])
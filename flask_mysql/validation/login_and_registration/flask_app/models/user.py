from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_app.models import items

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
  db_name = 'login_and_registration_schema'

  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.dob = data['dob']

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  @staticmethod
  def validate_email(data, category='register'):
    is_valid = True
    query = 'SELECT * FROM users WHERE email= %(email)s ;'
    if len(connectToMySQL('login_and_registration_schema').query_db(query, data)) > 0:
      flash("Email address already taken!", category)
      is_valid = False
    if not EMAIL_REGEX.match(data['email']):
      flash("Invalid email address!", category)
      is_valid = False
    return is_valid

  @staticmethod
  def validate_user(user, category='register'):
    is_valid = True
    if len(user['first_name'])<2:
      flash('First name must be at least 2 characters.', category)
      is_valid = False
    if len(user['last_name'])<2:
      flash('Last name must be at least 2 characters.', category)
      is_valid = False
    if not user['first_name'].isalpha():
      flash('First name may only contain letters.', category)
      is_valid = False
    if not user['last_name'].isalpha():
      flash('Last name may only contain letters.', category)
      is_valid = False
    if len(user['password'])<8:
      flash('Password must be at least 8 characters.', category)
      is_valid = False
    if user['password']!=user['password_confirm']:
      flash('Passwords do not match.', category)
      is_valid = False
    pw = user['password']
    if not all([any(char.isnumeric() for char in pw), any(char.isupper() for char in pw), any(char.islower() for char in pw)]):
      flash('Password requires at least 1 number, 1 uppercase, and 1 lowercase characters.', category)
      is_valid = False
    return is_valid

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO users (first_name, last_name, email, password, dob) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , %(dob)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_by_email(cls, data):
      query = "SELECT * FROM users WHERE email = %(email)s;"
      result = connectToMySQL(cls.db_name).query_db(query, data)
      if len(result) < 1:
          return False
      return cls(result[0])

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM users;'
    results = connectToMySQL(cls.db_name).query_db(query)
    users = []
    for row in results:
      users.append(cls(row))
    return users
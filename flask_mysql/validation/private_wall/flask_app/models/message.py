from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import datetime
import re
from flask_app.models import user

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Message:
  db_name = 'login_and_registration_schema'

  def __init__(self, data):
    self.id = data['id']
    self.message = data['message']
    self.user_id = data['user_id']
    self.recipient_id = data['recipient_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user = None

  def age(self):
    age = datetime.datetime.now()-self.updated_at
    if int(age.days) > 0:
      return f'{age.days} day(s)'
    elif int(age.seconds/3600) > 0:
      return f'{int(age.seconds/3600)} hour(s)'
    elif int(age.seconds/60) > 0:
      return f'{int(age.seconds/60)} minute(s)'
    return 'less than a minute'

  @staticmethod
  def validate_message(data):
    is_valid = True
    if len(data['message'])<5:
      is_valid = False
      flash('Message must be at least 5 characters long.')
    return is_valid

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO messages (message, user_id, recipient_id) VALUES ( %(message)s , %(user_id)s , %(recipient_id)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def get_one(cls, data):
    query = 'SELECT * FROM messages WHERE id = %(id)s ;'
    return cls(connectToMySQL(cls.db_name).query_db(query, data)[0])

  @classmethod
  def delete(cls, data):
    query = 'DELETE FROM messages WHERE id = %(id)s ;'
    return connectToMySQL(cls.db_name).query_db(query, data)

  @classmethod
  def user_messages(cls, data):
    query = 'SELECT * FROM messages JOIN users ON users.id = messages.user_id WHERE recipient_id = %(recipient_id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    messages = []
    for row in results:
      one_message = cls(row)
      user_data = {
        'id' : row['users.id'],
        'created_at' : row['users.created_at'],
        'updated_at' : row['users.updated_at'],
        'first_name' : row['first_name'],
        'last_name' : row['last_name'],
        'email' : row['email'],
        'password' : row['password'],
        'dob' : row['dob'],
      }
      one_message.user = user.User(user_data)
      messages.append(one_message)
    return messages

  @classmethod
  def message_count(cls, data):
    query = 'SELECT COUNT(messages.id) as count FROM messages JOIN users ON messages.user_id = users.id WHERE users.id = %(user_id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    return results[0]['count']

    

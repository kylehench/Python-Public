from flask_app.config.mysqlconnection import connectToMySQL

class User:
  db_name = 'friendships_schema'

  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.friends = []

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM users'
    results = connectToMySQL(cls.db_name).query_db(query)
    users = []
    for row in results:
      users.append(cls(row))
    return users

  @classmethod
  def get_friends(cls):
    query = 'SELECT * FROM users JOIN friendships ON users.id=friendships.user_id LEFT JOIN users as users2 ON friendships.friend_id=users2.id;'
    results = connectToMySQL(cls.db_name).query_db(query)
    friends = []
    for row in results:
      friend_data = {
        'first_name' : row['users2.first_name'],
        'last_name' : row['users2.last_name'],
        'id' : None,
        'created_at' : None,
        'updated_at' : None
      }
      friends.append([cls(row), cls(friend_data)])
    return friends
    

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO users (first_name, last_name) VALUES ( %(first_name)s , %(last_name)s );'
    id = connectToMySQL(cls.db_name).query_db(query, data)
    return id

  @classmethod
  def friendships_create(cls, data):
    query = 'INSERT INTO friendships (user_id, friend_id) VALUES ( %(user_id)s , %(friend_id)s );'
    id = connectToMySQL(cls.db_name).query_db(query, data)
    return id

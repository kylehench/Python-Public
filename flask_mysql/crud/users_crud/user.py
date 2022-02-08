# import the function that will return the instance of a connection
from mysqlconnection import connectToMySQL
class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
  
  # class method to query our database
  @classmethod
  def get_all(cls):
    query = "SELECT * from users;"
    results = connectToMySQL('users_schema').query_db(query)
    users = []
    for user in results:
      users.append(cls(user))
    return users

  # class method to query one user from our database
  @classmethod
  def get_id(cls, id):
    data = {'id' : id}
    query = "SELECT * from users WHERE id= %(id)s ;"
    results = connectToMySQL('users_schema').query_db(query, data)
    users = []
    for user in results:
      users.append(cls(user))
    return users

  # class method to save our user to the database
  @classmethod
  def save(cls, data):
      query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
      # data is a dictionary that will be passed into the save method from server.py
      return connectToMySQL('users_schema').query_db( query, data )

  # class method to update a user in the database
  @classmethod
  def update_id(cls, data):
      query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id=%(id)s;"
      connectToMySQL('users_schema').query_db(query, data)

  # class method to delete a user in the database
  @classmethod
  def delete_id(cls, id):
      data = {'id' : id}
      query = "DELETE FROM users WHERE id= %(id)s ;"
      connectToMySQL('users_schema').query_db(query, data)
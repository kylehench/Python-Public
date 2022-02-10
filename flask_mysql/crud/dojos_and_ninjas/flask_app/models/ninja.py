from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.dojo_id = data['dojo_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.dojo = None

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM ninjas JOIN dojos ON dojos.id = dojos_id'
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    ninjas = []
    for result in results:
      ninja = cls(result)
      dojo_data = {
        'id' : result['dojos.id'],
        'name' : result['name'],
        'created_at' : result['dojos.created_at'],
        'updated_at' : result['dojos.updated_at'],
      }
      ninja.dojo = dojo.Dojo(dojo_data)
      ninjas.append(ninja)
    return ninjas

  @classmethod
  def save(cls, data):
    query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s );'
    return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
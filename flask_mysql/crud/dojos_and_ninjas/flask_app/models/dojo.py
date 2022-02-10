from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.ninjas = []

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM dojos;'
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    dojos = []
    for dojo in results:
      dojos.append(cls(dojo))
    return dojos

  @classmethod
  def get_one_with_ninjas(cls, id):
    query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;'
    data = {'id' : id}
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    dojo = Dojo(results[0])
    for result in results:
      ninja_data = {
        'id' : result['ninjas.id'],
        'first_name' : result['first_name'],
        'last_name' : result['last_name'],
        'age' : result['age'],
        'dojo_id' : result['dojo_id'],
        'created_at' : result['ninjas.created_at'],
        'updated_at' : result['ninjas.updated_at']
      }
      dojo.ninjas.append(ninja.Ninja(ninja_data))
    return dojo

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO dojos (name) VALUES ( %(name)s );'
    return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
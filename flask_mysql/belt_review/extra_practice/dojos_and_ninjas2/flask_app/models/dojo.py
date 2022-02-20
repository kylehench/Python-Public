from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import ninja

class Dojo:
  db_name = 'python-exam-practice'

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.ninjas = []

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM dojos;'
    return [cls(result) for result in connectToMySQL(cls.db_name).query_db(query)]

  @classmethod
  def get_one_with_ninjas(cls, data):
    query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s ;'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    dojo = cls(results[0])
    for row in results:
      if row['ninjas.id'] == None:
        break
      ninja_data = {
        'id' : row['ninjas.id'],
        'created_at' : row['ninjas.created_at'],
        'updated_at' : row['ninjas.updated_at'],
        'first_name' : row['first_name'],
        'last_name' : row['last_name'],
        'age' : row['age'],
        'dojo_id' : row['dojo_id'],
      }
      dojo.ninjas.append(ninja.Ninja(ninja_data))
    return dojo

  @classmethod
  def create(cls, data):
    query = 'INSERT INTO dojos (name) VALUES ( %(name)s );'
    return connectToMySQL(cls.db_name).query_db(query, data)
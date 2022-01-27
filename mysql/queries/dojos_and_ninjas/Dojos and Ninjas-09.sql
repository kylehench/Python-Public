SELECT name, ninjas.first_name FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 11;
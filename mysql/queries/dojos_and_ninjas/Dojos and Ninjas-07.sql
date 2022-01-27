SELECT first_name, last_name, dojos.name FROM ninjas
LEFT JOIN dojos ON dojo_id = dojos.id;
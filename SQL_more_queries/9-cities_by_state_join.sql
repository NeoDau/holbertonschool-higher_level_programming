-- city by states --
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON states.id = state_id ORDER BY cities.id;

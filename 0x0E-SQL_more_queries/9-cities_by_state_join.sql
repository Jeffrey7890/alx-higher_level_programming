-- list all cities contained in the database
-- sorted in ascending order by cities.id
SELECT DISTINCT cities.id, cities.name, states.name FROM cities JOIN states
	WHERE cities.state_id = states.id ORDER BY cities.id ASC;

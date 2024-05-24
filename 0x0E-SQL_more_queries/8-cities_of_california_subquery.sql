-- lists all cities of california
-- in ascending order of cities id

SELECT * FROM cities WHERE state_id = (
	SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;

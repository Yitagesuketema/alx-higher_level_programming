-- lists all the cities of California that can be found
-- in the database hbtn_0d_usa ,
-- sorted in ascending order by cities.id.

SELECT * FROM hbtn_0d_usa.cities
WHERE name = California ORDER BY cities.id
DESC;

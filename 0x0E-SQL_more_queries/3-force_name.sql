-- creates the table force_name on mysql server
-- if it doesn't exist
-- id INT
-- name VARCHAR(256) can't be null
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

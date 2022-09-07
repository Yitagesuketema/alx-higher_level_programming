 -- creates the database hbtn_0d_usa on mysql server
 -- if not exists.

 CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates  table 'cities' in the database 'hbtn_0d_usa'
-- if not exists,
-- id INT unique, auto generated, can’t be null and is a primary key,
-- state_id INT, can’t be null and must be a FOREIGN KEY ,
--  that references to id of the states table ,
-- name VARCHAR(256) can’t be null.

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL ,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
 );

-- creates the database hbtn_0d_usa if not exists.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table 'states' in the database 'hbtn_0d_usa' if not exists,
-- id INT unique, auto generated, can’t be null and is a primary key,
-- name VARCHAR(256) can’t be null.

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (

 id INT UNIQUE AUTO_INCREMENT,
 name VARCHAR(256) NOT NULL,
 PRIMARY KEY (id)

 );

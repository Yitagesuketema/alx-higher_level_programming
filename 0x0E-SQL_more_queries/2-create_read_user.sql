-- create the database hbtn_0d_2 if not exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user user_0d_2 @ localhost with pasword user_0d_1_pwd.
CREATE USER  IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- grant SELECT privileges to user user_0d_2 at local host.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;

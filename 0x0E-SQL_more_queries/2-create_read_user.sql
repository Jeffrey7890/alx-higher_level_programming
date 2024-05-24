-- create user_0d_1 if not exists
-- grants all privileges to user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'User_0d_2_pw#d';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- creates a database hbtn_0d_usa and the table states
-- states (id INT UNIQUE AUTOINCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);


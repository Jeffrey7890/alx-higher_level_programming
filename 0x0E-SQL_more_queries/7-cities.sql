-- creates hbtn_0d_usa database with cities table
-- cities (id INT AUTO_INCREMENT PRIMARY KEY, state_id INT FOREIGN KEY,
-- name VARCHAR(256) NOT NULL)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	INDEX sta_ind (state_id),
	FOREIGN KEY (state_id)
		REFERENCES states(id)
);

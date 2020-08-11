CREATE DATABASE galaxy;
USE galaxy;
CREATE TABLE news_type(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	type VARCHAR(20) NOT NULL UNIQUE
)
INSERT INTO news_type(type) VALUE("Finance"),("World"),("National"),("Technology");

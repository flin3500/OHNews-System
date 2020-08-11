CREATE TABLE news_user(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(20) NOT NULL UNIQUE,
	password VARCHAR(500) NOT NULL,
	email VARCHAR(100) NOT NULL,
	role_id INT UNSIGNED NOT NULL,
	INDEX(username)
);

INSERT INTO news_user(username, password, email, role_id)
VALUE("Admin",HEX(AES_ENCRYPT("123456","HelloWorld")), "admin@gmail.com", 1);

INSERT INTO news_user(username, password, email, role_id)
VALUE("Will",HEX(AES_ENCRYPT("123456","HelloWorld")), "will@gmail.com", 2);

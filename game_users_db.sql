CREATE DATABASE game_users_db;

USE game_users_db;

CREATE TABLE users (
    user_id INTEGER AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
	PRIMARY KEY(user_id)
);

CREATE TABLE game_statistics (
    statistics_id INTEGER AUTO_INCREMENT,
    user_id INT,
    points INT DEFAULT 0,
    life INT DEFAULT 3, -- Assuming 3 is full life
    level INT DEFAULT 1,
    PRIMARY KEY(statistics_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
CREATE DATABASE game_users_db;

USE game_users_db;

CREATE TABLE users (
    user_id INTEGER AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(150) NOT NULL,
	PRIMARY KEY(user_id)
);

CREATE TABLE game_statistics (
    statistics_id INTEGER AUTO_INCREMENT,
    user_id INT,
    points INT DEFAULT 0,
    life INT DEFAULT 90, -- Assuming 90 is full life
    level INT DEFAULT 1,
    PRIMARY KEY(statistics_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users
(username, password)
VALUES
('TestCat', 'Testtest1!'),
('TestDog', 'Testtest1!'),
('TestHamster', 'Testtest1!'),
('TestBird', 'Testtest1!'),
('TestRabbit', 'Testtest1!'),
('TestSnake', 'Testtest1!'),
('TestDuck', 'Testtest1!'),
('TestWhale', 'Testtest1!');

INSERT INTO game_statistics
(user_id, points, life, level)
VALUES
(1, 10, 5, 2),
(2, 20, 80, 1),
(3, 5, 65, 1),
(4, 35, 75, 2),
(5, 10, 60, 2),
(6, 40, 10, 2),
(7, 55, 20, 1),
(8, 0, 90, 1);

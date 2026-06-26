CREATE DATABASE student_management;

USE student_management;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10),
    course VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
# student-management-system-python-mysql
# Student Management System

A Python and MySQL based Student Management System that performs CRUD operations on student records.

## Features

- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

## Technologies Used

- Python
- MySQL
- SQL
- mysql-connector-python

## Database Schema

students

| Field | Type |
|---------|---------|
| student_id | INT (PK) |
| name | VARCHAR(100) |
| age | INT |
| gender | VARCHAR(10) |
| course | VARCHAR(100) |
| email | VARCHAR(100) |

## Installation

1. Create database using database.sql
2. Update MySQL credentials in db.py
3. Install requirements

pip install -r requirements.txt

4. Run

python main.py

## Author

Pallavi Kumari
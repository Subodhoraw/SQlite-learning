SQL learning guide

A comprehensive guide to learning SQLite, a lightweight, serverless relational database management system.

Table of Contents
What is SQLite?

Installation

Basic Commands

SQL Operations

Advanced Features

Practice Exercises

Resources

What is SQLite?
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured SQL database engine. It is the most used database engine in the world and is built into all mobile phones and most computers.

Key Features:

Serverless (no separate server process)

Zero-configuration

Transactional (ACID compliant)

Cross-platform

Lightweight (complete database in a single file)

Installation
Windows
Download precompiled binaries from sqlite.org

Add SQLite to your PATH environment variable

macOS
bash
# Using Homebrew
brew install sqlite3
Linux
bash
# Ubuntu/Debian
sudo apt install sqlite3

# CentOS/RHEL
sudo yum install sqlite3
Basic Commands
Starting SQLite
bash
# Open or create a database
sqlite3 mydatabase.db

# Open in-memory database
sqlite3 :memory:
Basic SQLite Shell Commands
sql
.help                    -- Show all commands
.tables                  -- List all tables
.schema [table]          -- Show table structure
.databases               -- Show connected databases
.mode [mode]             -- Set output mode (csv, column, html, etc.)
.headers on/off          -- Show/hide column headers
.quit                    -- Exit SQLite
SQL Operations
Creating Tables
sql
-- Create a simple table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create table with foreign key
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT NOT NULL,
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
Basic CRUD Operations
Create (INSERT)
sql
INSERT INTO users (name, email, age) 
VALUES ('John Doe', 'john@example.com', 30);

INSERT INTO users (name, email, age) 
VALUES 
    ('Jane Smith', 'jane@example.com', 25),
    ('Bob Wilson', 'bob@example.com', 35);
Read (SELECT)
sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT name, email FROM users;

-- With WHERE clause
SELECT * FROM users WHERE age > 25;

-- With ORDER BY
SELECT * FROM users ORDER BY age DESC;

-- With LIMIT
SELECT * FROM users LIMIT 5;
Update (UPDATE)
sql
UPDATE users 
SET age = 31, email = 'john.doe@example.com' 
WHERE id = 1;
Delete (DELETE)
sql
DELETE FROM users WHERE id = 3;
Advanced Queries
JOIN Operations
sql
-- INNER JOIN
SELECT users.name, posts.title, posts.content
FROM users
INNER JOIN posts ON users.id = posts.user_id;

-- LEFT JOIN
SELECT users.name, COUNT(posts.id) as post_count
FROM users
LEFT JOIN posts ON users.id = posts.user_id
GROUP BY users.id;
Aggregate Functions
sql
-- Count
SELECT COUNT(*) FROM users;

-- Average age
SELECT AVG(age) FROM users;

-- Group by with having
SELECT age, COUNT(*) as count
FROM users
GROUP BY age
HAVING COUNT(*) > 1;
Subqueries
sql
-- Users older than average age
SELECT name, age 
FROM users 
WHERE age > (SELECT AVG(age) FROM users);
Advanced Features
Transactions
sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
-- or ROLLBACK; in case of error
Indexes
sql
-- Create index for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_age ON users(age);

-- Show indexes
.indices users
Views
sql
-- Create a view
CREATE VIEW user_posts AS
SELECT users.name, posts.title, posts.content
FROM users
JOIN posts ON users.id = posts.user_id;

-- Use the view
SELECT * FROM user_posts;
Triggers
sql
-- Create a trigger for audit logging
CREATE TABLE user_audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER user_update_trigger 
AFTER UPDATE ON users
BEGIN
    INSERT INTO user_audit (user_id, action) 
    VALUES (OLD.id, 'UPDATE');
END;
Practice Exercises
Exercise 1: Library Database
Create a database for a library system:

sql
-- Create tables for books, authors, and borrowers
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    published_year INTEGER,
    isbn TEXT UNIQUE,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE borrowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT
);

CREATE TABLE loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    borrower_id INTEGER,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
);
Exercise 2: Queries
Write queries to:

Find all books by a specific author

Count books published each year

Find borrowers with overdue books

Calculate average loan duration

Sample Project: Personal Task Manager
Create a simple task management database:

sql
-- Tasks table
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    priority INTEGER DEFAULT 1,
    status TEXT DEFAULT 'pending',
    due_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME
);

-- Categories table
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Task-categories relationship
CREATE TABLE task_categories (
    task_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (task_id, category_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Sample data
INSERT INTO categories (name) VALUES 
('Work'), ('Personal'), ('Shopping'), ('Health');

INSERT INTO tasks (title, description, priority, due_date) VALUES
('Complete report', 'Finish quarterly report', 2, '2024-02-15'),
('Buy groceries', 'Milk, eggs, bread', 1, '2024-02-10');
Resources
Documentation
Official SQLite Documentation

SQLite SQL Reference

Online Tools
SQLite Online Editor

DB Browser for SQLite

Learning Resources
SQLite Tutorial

W3Schools SQLite Tutorial

Books
"Using SQLite" by Jay A. Kreibich

"SQLite Pocket Reference" by Chris Newman

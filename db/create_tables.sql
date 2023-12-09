-- For testing purposes. To be deleted
DROP TABLE IF EXISTS Users;

-- For testing purposes. To be deleted
DROP TABLE IF EXISTS Orders;

-- For testing purposes. To be deleted
DROP TABLE IF EXISTS Books;

-- Creates Users table
CREATE TABLE IF NOT EXISTS
    Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL
    );

-- Creates Orders table
CREATE TABLE IF NOT EXISTS
    Orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT NOT NULL,
        -- address TEXT NOT NULL,
        book_list TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users (id) -- Relationship Users 1..* Orders
    );

-- Creates Books table
CREATE TABLE IF NOT EXISTS
    Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        stock INTEGER NOT NULL,
        price REAL NOT NULL
    );

-- Queries to add some testing values to the database


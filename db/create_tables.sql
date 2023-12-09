-- ATTACH DATABASE './Bookstore.db' as Bookstore; -- This line should be run once when starting the app
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
        password TEXT NOT NULL,
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
INSERT INTO
    Users (fname, lname, login, password, salt, role)
VALUES
    ('b', 'j', 'bj', 'pass', '1', 'admin');

INSERT INTO
    Orders (
        date,
        priority,
        status,
        address,
        book_list,
        user_id
    )
VALUES
    (
        '07.12.2023',
        'high',
        'in progress',
        'essa 23/1',
        '{"dziady": 1}',
        1
    );

INSERT INTO
    Books (name, author, stock, price)
VALUES
    ('dziady', 'mickiewicz', 10, 5.99);

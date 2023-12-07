-- ATTACH DATABASE './Bookstore.db' as Bookstore;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL,
    role TEXT NOT NULL
);

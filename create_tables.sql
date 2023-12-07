-- ATTACH DATABASE './Bookstore.db' as Bookstore;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Orders;

CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    address TEXT NOT NULL,
    book_list TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);


-- INSERT INTO Users (fname, lname, login, password, salt, role)
-- VALUES
-- ('b', 'j', 'bj', 'pass', '1', 'admin');

-- INSERT INTO Orders (date, priority, status, address, book_list, user_id)
-- VALUES
-- ('07.12.2023', 'high', 'in progress', 'essa 23/1', '{"dziady": 1}', 1);

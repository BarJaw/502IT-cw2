INSERT INTO
    Users (fname, lname, username, password_hash, role)
VALUES
    ('b', 'j', 'bj', 'pass', 'admin');

INSERT INTO
    Orders (date, priority, status, book_list, user_id)
VALUES
    (
        '07.12.2023',
        'high',
        'in progress',
        '{"dziady": 1}',
        1
    );

INSERT INTO
    Books (name, author, stock, price)
VALUES
    ('dziady', 'mickiewicz', 10, 5.99);
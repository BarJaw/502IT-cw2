INSERT INTO
    Users (fname, lname, username, password_hash, role)
VALUES
    (
        'b',
        'j',
        'bj2',
        '$2a$12$LiTzvF55MoKtPCLdtWqOMuc5u4knQiiz3oTUeaC1Jqb3v6k.ySIAO',
        'employee'
    );

INSERT INTO
    Orders (date, priority, status, amount, book_list, user_id)
VALUES
    (
        '07.12.2023',
        'high',
        'waiting for acceptance',
        10.99,
        '{"dziady": 1}',
        1
    );

INSERT INTO
    Books (name, author, stock, price)
VALUES
    ('dziady cz. 1', 'mickiewicz', 10, 5.99),
    ('dziady cz. 2', 'mickiewicz', 10, 5.99),
    ('dziady cz. 3', 'mickiewicz', 10, 5.99),
    ('dziady cz. 4', 'mickiewicz', 10, 5.99);

DELETE FROM Users
WHERE
    username = 'nednik';
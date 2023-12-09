INSERT INTO
    Users (fname, lname, username, password_hash, role)
VALUES
    ('b', 'j', 'bj', '$2a$12$LiTzvF55MoKtPCLdtWqOMuc5u4knQiiz3oTUeaC1Jqb3v6k.ySIAO', 'admin');

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
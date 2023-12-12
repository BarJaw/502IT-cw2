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
    Orders (
        date,
        priority,
        status,
        address,
        estimated_date_of_arrival,
        amount,
        book_list,
        user_id
    )
VALUES
    (
        '07.12.2023',
        'high',
        'waiting for acceptance',
        'Wroclaw, aaa',
        '12.12.2023',
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

INSERT INTO
    Cities (city, shipment_time)
VALUES
    ('Warszawa', 2),
    ('Kraków', 1),
    ('Łódź', 3),
    ('Wrocław', 2),
    ('Poznań', 1),
    ('Gdańsk', 3),
    ('Szczecin', 1),
    ('Bydgoszcz', 2),
    ('Lublin', 3),
    ('Białystok', 1),
    ('Katowice', 2),
    ('Gdynia', 3),
    ('Częstochowa', 1),
    ('Radom', 2),
    ('Sosnowiec', 3),
    ('Toruń', 1),
    ('Kielce', 2),
    ('Rzeszów', 3),
    ('Gliwice', 1),
    ('Zabrze', 2),
    ('Olsztyn', 3),
    ('Bielsko-Biała', 1),
    ('Bytom', 2),
    ('Zielona Góra', 3)
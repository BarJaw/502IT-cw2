INSERT INTO
    Users (fname, lname, username, password_hash, role)
VALUES
    (
        'Bartosz',
        'Jaworski',
        'bj3',
        '$2a$12$LiTzvF55MoKtPCLdtWqOMuc5u4knQiiz3oTUeaC1Jqb3v6k.ySIAO',
        'customer'
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
    ('Dziady cz. 1', 'Mickiewicz', 10, 5.99),
    ('Pan Tadeusz', 'Mickiewicz', 15, 7.99),
    ('Quo Vadis', 'Sienkiewicz', 8, 6.49),
    ('Krzyżacy', 'Sienkiewicz', 12, 8.99),
    ('Шантарам', 'Roberts', 20, 12.99),
    ('Метро 2033', 'Глуховский', 25, 9.99),
    ('Українська кухня', 'Шевченко', 18, 15.49),
    ('Вий', 'Гоголь', 7, 4.99),
    ('The Vegetarian', 'Han Kang', 30, 11.99),
    ('Pachinko', 'Min Jin Lee', 22, 13.99),
    ('1Q84', 'Haruki Murakami', 14, 10.49),
    ('Norwegian Wood', 'Haruki Murakami', 18, 9.99),
    ('Crime and Punishment', 'Dostoevsky', 15, 8.99),
    ('The Brothers Karamazov', 'Dostoevsky', 12, 9.99),
    ('War and Peace', 'Tolstoy', 20, 12.49),
    ('Anna Karenina', 'Tolstoy', 17, 10.99),
    ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 25, 11.99),
    ('Love in the Time of Cholera', 'Gabriel Garcia Marquez', 18, 9.49),
    ('The Master and Margarita', 'Bulgakov', 10, 7.99),
    ('The Idiot', 'Dostoevsky', 12, 8.49),
    ('Solaris', 'Stanisław Lem', 15, 11.99),
    ('Щоденник', 'Тарас Шевченко', 10, 6.99),
    ('Мацеба', 'Марко Вовчок', 8, 5.99),
    ('Десятикласники', 'Іван Франко', 14, 7.99),
    ('Kobiety', 'Witkacy', 16, 8.99),
    ('Dywizjon 303', 'Arkady Fiedler', 20, 9.99),
    ('Ziemia Obiecana', 'Reymont', 15, 10.49),
    ('Lalka', 'Bolesław Prus', 12, 8.99),
    ('Opium w rosole', 'Hanna Ożogowska', 18, 7.99),
    ('Kordian', 'Słowacki', 22, 9.49),
    ('Jądro ciemności', 'Joseph Conrad', 20, 10.99),
    ('Zbrodnia i kara', 'Dostojewski', 15, 11.99),
    ('Niezwyciężony', 'Stanisław Lem', 18, 12.99),
    ('Przedwiośnie', 'Stefan Żeromski', 25, 13.99),
    ('Dziennik', 'Leopold Tyrmand', 30, 14.49),
    ('Solaris', 'Stanisław Lem', 12, 9.99),
    ('Dżuma', 'Albert Camus', 14, 10.99),
    ('Idiota', 'Fiodor Dostojewski', 16, 11.99),
    ('Kolos', 'Bogusław Wołoszański', 18, 12.49),
    ('Zielona mila', 'Stephen King', 20, 13.99),
    ('Wojna i pokój', 'Lew Tołstoj', 22, 14.99),
    ('Sto lat samotności', 'Gabriel Garcia Marquez', 24, 15.49),
    ('Pani Bovary', 'Gustave Flaubert', 26, 16.49),
    ('Obcy', 'Albert Camus', 28, 17.49),
    ('Kraina Midianu', 'Clive Barker', 30, 18.49),
    ('Stacja Dune', 'Frank Herbert', 32, 19.49),
    ('Złodziejka książek', 'Markus Zusak', 34, 20.49),
    ('Nie opuszczaj mnie', 'Kazuo Ishiguro', 36, 21.49),
    ('Marsjanin', 'Andy Weir', 38, 22.49),
    ('Igrzyska śmierci', 'Suzanne Collins', 40, 23.49),
    ('Harry Potter i Kamień Filozoficzny', 'J.K. Rowling', 42, 24.49),
    ('Morderstwo w Orient Expressie', 'Agatha Christie', 44, 25.49),
    ('Szklany tron', 'Sarah J. Maas', 46, 26.49),
    ('Cieniutka nitka', 'Ken Follett', 48, 27.49),
    ('Dzieci Diuny', 'Frank Herbert', 50, 28.49),
    ('Władca Pierścieni', 'J.R.R. Tolkien', 52, 29.49),
    ('Gra o tron', 'George R.R. Martin', 54, 30.49),
    ('Mroczna Wieża', 'Stephen King', 56, 31.49),
    ('Ostatnie życzenie', 'Andrzej Sapkowski', 58, 32.49),
    ('Nielegalni', 'Dan Krokos', 60, 33.49),
    ('Obca', 'Alan Dean Foster', 62, 34.49),
    ('Taniec ze smokami', 'George R.R. Martin', 64, 35.49),
    ('Zdążyć przed Panem Bogiem', 'Gabriela Zapolska', 66, 36.49),
    ('Dymy nad Birkenau', 'Seweryna Szmaglewska', 68, 37.49),
    ('Stary człowiek i morze', 'Ernest Hemingway', 70, 38.49);




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
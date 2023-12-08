import sqlite3
import bcrypt

class UserDatabase:
    def __init__(self, database_name='user_database.db'):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self.conn.commit()

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

class AuthSystem:
    def __init__(self, user_db):
        self.user_db = user_db

    def register(self):
        print("\033[94m=== Registration ===\033[0m")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        existing_user = self.user_db.get_user(username)
        if existing_user:
            print("\033[91m=== Username already exists. Please choose another one\033[0m")
        else:
            self.user_db.register_user(username, password)
            print("\033[92m=== Registration successful! ===\033[0m")

    def login(self):
        print("\033[94m=== Login ===\033[0m")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = self.user_db.get_user(username)
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
            print("\033[92m=== Login successful! ===\033[0m")
        else:
            print("\033[91m=== Invalid username or password ===\033[0m")

def main():
    user_db = UserDatabase()
    auth_system = AuthSystem(user_db)

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("\033[94mChoose an option: \033[0m")

        if choice == "1":
            auth_system.register()
        elif choice == "2":
            auth_system.login()
        elif choice == "3":
            break
        else:
            print("\033[91m=== Invalid choice. Please choose again\033[0m")

    user_db.close_connection()

if __name__ == "__main__":
    main()

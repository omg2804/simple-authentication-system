import sqlite3

class Database:
    def __init__(self, db_name=':memory:'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_user_table()

    def create_user_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_user(self, username, password):
        self.cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()

    def update_user(self, username, new_password):
        self.cursor.execute('''
            UPDATE users SET password = ? WHERE username = ?
        ''', (new_password, username))
        self.connection.commit()

    def delete_user(self, username):
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.connection.commit()

    def close(self):
        self.connection.close()
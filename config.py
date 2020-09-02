import sqlite3

class SQLite:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
    
    def add_user(self, user_id, name, surname, gender, email, b_date, height):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, name, surname, gender, email, b_date, height))
    
    def get_ids(self):
        with self.connection:
            return self.cursor.execute(f"SELECT id FROM user").fetchall()
    
    def find_id(self, user_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM user WHERE id = '{user_id}'").fetchall()
            return bool(result)
    
    def get_set(self, user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT birthdate, height FROM user WHERE id = '{user_id}'").fetchone()
    
    def find_athlete(self):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM athelete").fetchall()
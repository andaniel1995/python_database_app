import psycopg2
import os


class Database:

    def __init__(self):
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")

    def get_db_connection(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        return conn

    def create_table(self):
        conn = self.get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS names (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL
                );
            ''')
            conn.commit()
        conn.close()

    def add_name(self, first_name, last_name):
        conn = self.get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO names (first_name, last_name) VALUES (%s, %s)',
                (first_name, last_name)
            )
            conn.commit()
        conn.close()

    def delete_name(self, first_name, last_name):
        conn = self.get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                'DELETE FROM names WHERE first_name = %s AND last_name = %s',
                (first_name, last_name)
            )
            conn.commit()
        conn.close()

    def get_names(self):
        conn = self.get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('SELECT first_name, last_name FROM names')
            names = cursor.fetchall()
        conn.close()
        return names

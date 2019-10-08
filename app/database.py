import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database:

    def __init__(self):
        
        self.conn = psycopg2.connect(
        dbname="karibu",
        user="postgres",
        password="Alimanu195ogwal",
        host="localhost",
        port="5432"
        )
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.create_user_table()

        print("Connected to karibu")

    def create_user_table(self):
        user_table = "CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY, \
            username varchar(50), email varchar(30), password varchar(256))"

        self.cur.execute(user_table)
    
import sqlite3
import os 
def create_connection(db_file="learning.db"):
    """create a database connection to the sqlite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"error connecting to database:{e}")
        return conn
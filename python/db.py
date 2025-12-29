# slqite db connect method
import sqlite3

def connect_db():
    conn = sqlite3.connect('project.db')
    conn.row_factory = sqlite3.Row
    print("Database connected successfully.")
    return conn
import sqlite3

def get_connection():
    return sqlite3.connect("focuslens.db")

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY AUTOINCREMENT, session_date TEXT, time_period TEXT, duration INTEGER, energy_level TEXT, task_type TEXT)"
    )
    connection.commit()
    connection.close()
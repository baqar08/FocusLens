import sqlite3

def get_db_connection():
    conn = sqlite3.connect('focuslens.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time_period TEXT NOT NULL,
            duration INTEGER NOT NULL,
            energy_level INTEGER NOT NULL,
            task_type TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

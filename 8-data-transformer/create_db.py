import sqlite3


def create_db():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("nayya.db")

    # Create a cursor object
    cursor = conn.cursor()

    

    # Commit changes and close the connection
    conn.commit()
    conn.close()

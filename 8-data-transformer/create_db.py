import sqlite3


def create_db():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("nayya.db")

    # Create a cursor object
    cursor = conn.cursor()

    # Create a Nayya Enrollments table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS nayya_enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        internal_id TEXT,
        group_id TEXT,
        group_name TEXT,
        plan_id TEXT,
        gender VARCHAR(1),
        relationship_code INTEGER,
        enrollment_start_date DATE,
        enrollment_end_date DATE,
        benefit_type TEXT,
        benefit_max INTEGER,
        benefit_minimum INTEGER,
        benefit_spread INTEGER
    )
    """
    )

    # Commit changes and close the connection
    conn.commit()
    conn.close()

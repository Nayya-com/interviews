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
        person_id TEXT NOT NULL,
        group_id TEXT NOT NULL,
        group_name TEXT NOT NULL,
        plan_id TEXT NOT NULL,
        gender VARCHAR(1) NOT NULL,
        relationship_code INTEGER NOT NULL,
        enrollment_start_date DATE NOT NULL,
        enrollment_end_date DATE NOT NULL,
        benefit_type TEXT,
        benefit_minimum INTEGER,
        benefit_max INTEGER,
        benefit_spread INTEGER
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS relationship_codes_mapping (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        relationship_code INTEGER,
        relationship_name TEXT
    )
    """
    )

    cursor.execute(
        """
        INSERT INTO relationship_codes_mapping (relationship_code, relationship_name)
        VALUES
            (1, "Subscriber"),
            (2, "Spouse"),
            (3, "Dependent"),
            (4, "Other")
        """
    )

    # Commit changes and close the connection
    conn.commit()
    conn.close()

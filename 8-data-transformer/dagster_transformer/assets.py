import sqlite3
from code.transformer import config_column_transformer

import dagster as dg
import pandas as pd


@dg.asset
def read_sample_enrollment_data() -> pd.DataFrame:
    """Sample asset showing pandas and sqlalchemy usage."""
    df = pd.read_csv("data/DECodePairingInterview2025.csv")
    return df


@dg.asset
def transform_enrollment_data(read_sample_enrollment_data: pd.DataFrame) -> pd.DataFrame:
    """
    This asset transforms the enrollment data so it can be written to the database

    Args:
        read_sample_enrollment_data (pd.DataFrame): The enrollment data to transform

    Returns:
        pd.DataFrame: The transformed enrollment data
    """
    # Transform columns to match the config
    df = config_column_transformer(read_sample_enrollment_data)

    return df


@dg.asset
def write_enrollment_data_to_db(transform_enrollment_data: pd.DataFrame) -> None:
    """Write enrollment data to the database"""
    pass

    # Connect to the SQLite database
    conn = sqlite3.connect("nayya.db")
    cursor = conn.cursor()

    df_entries = transform_enrollment_data.to_dict(orient="records")
    # Insert data into the database
    for row in df_entries:
        print(row)
        cursor.execute(
            """
        INSERT INTO nayya_enrollments (group_id, plan_id)
        VALUES (?, ?)
        """,
            (row["GroupID"], row["PlanID"]),
        )

    # Commit changes and close the connection
    conn.commit()
    conn.close()

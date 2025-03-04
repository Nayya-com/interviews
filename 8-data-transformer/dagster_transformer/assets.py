import sqlite3
from code.transformer import config_column_transformer, create_person_id

import dagster as dg
import pandas as pd


@dg.asset
def read_sample_enrollment_data() -> pd.DataFrame:
    """This asset reads in the raw enrollment CSV file."""
    df = pd.read_csv("data/raw_enrollments_202503.csv")
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

    # Create person id and strip PHI/PII from the data

    # Transform the relationship code

    #

    return df


@dg.asset
def write_enrollment_data_to_db(transform_enrollment_data: dict) -> None:
    """Write enrollment data to the database"""
    pass

    # Connect to the SQLite database
    conn = sqlite3.connect("nayya.db")
    cursor = conn.cursor()

    # Insert data into the database
    for row in transform_enrollment_data:
        print(row)
        cursor.execute(
            """
        INSERT INTO nayya_enrollments (person_id, group_id, group_name, plan_id, gender, relationship_code, enrollment_start_date, enrollment_end_date, benefit_type, benefit_max, benefit_minimum, benefit_spread)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                row["person_id"],
                row["group_id"],
                row["group_name"],
                row["plan_id"],
                row["gender"],
                row["relationship_code"],
                row["enrollment_start_date"],
                row["enrollment_end_date"],
                row["benefit_type"],
                row["benefit_minimum"],
                row["benefit_max"],
                row["benefit_spread"],
            ),
        )

    # Commit changes and close the connection
    conn.commit()
    conn.close()

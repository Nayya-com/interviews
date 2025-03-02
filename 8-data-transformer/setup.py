# import subprocess

from create_db import create_db

# def run_dagster_dev():
#     try:
#         subprocess.run(["dagster", "dev"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred: {e}")


def main():
    print("Welcome to your coding interview!")

    print("Creating database...")
    create_db()
    print("Database created successfully!")

    # print("Starting Dagster...")
    # run_dagster_dev()


if __name__ == "__main__":
    main()

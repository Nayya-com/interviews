# Data Transformer

Welcome to your coding interview!

## Summary
This test builds upon the previous system design test. Currently, we have a pipeline that extracts data from a CSV file and loads it into a database. We decided to go with YAML based config files as our configurable data mapping for ease of readability and maintainability. We need to apply certain transformations to the data in order to load it into the `nayya` database.

### Additional Background
- We use [dagster](https://docs.dagster.io/) to orchestrate our pipelines.
- We are using [SQLite](https://www.sqlite.org/index.html) as our database.
  - You can view the database using the SQLite Explorer in VSCode.
- You can view the raw data in `data/raw_enrollments_202503.csv`.
- The YAML base config is located in `config/field_mapping.yaml`



### Objectives
Create a pipeline that extracts data from the CSV file and loads it into a standardized table the database.

## Setup

<details> 
<summary>Setup should be completed pre-interview. Interviewee can skip this section. </summary>

Tools needed:
- VSCode: a popular code editor (https://code.visualstudio.com/)
- uv: a lightweight package manager for Python (https://docs.astral.sh/uv)
    - To install uv, run `curl -fsSL https://get.uv.dev | sh`
- SQLite Explorer: a SQLite database manager for VSCode (https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite)

1. Run `uv sync` to install the dependencies.
2. Run `uv run setup.py` This will create a database (`nayya.db`).
3. Run `dagster dev` to start the Dagster instance.
4. Connect to the database (`nayya.db`) using SQLite Explorer in VSCode: Ctrl+Shift+P -> SQLite: Connect -> Select Database ->nayya.db.
</details>

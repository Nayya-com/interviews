import pandas as pd
import yaml


def _load_config(config_path: str) -> dict:
    """
    Load the config file

    Args:
        config_path (str): The path to the config file

    Returns:
        dict: The config file
    """
    return {}


def config_column_transformer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Loads in the config file and transforms the dataframe columns to match the config

    Args:
        df (pd.DataFrame): The dataframe to transform

    Returns:
        pd.DataFrame: The transformed dataframe
    """
    path = "config/field_mappings.yaml"
    config = _load_config(path)

    # Transform DataFrame columns to match the config

    return df

import json
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "schemes.json"


def load_schemes(path=DATA_FILE):
    """Read schemes.json and return a list of scheme dictionaries."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def schemes_to_table(schemes):
    """Turn a list of scheme dictionaries into a Pandas table (DataFrame)."""
    return pd.DataFrame(schemes)
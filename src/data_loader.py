
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "survey_results_public.csv"


def load_data():
    """Load the Stack Overflow 2019 survey dataset."""

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    return pd.read_csv(DATASET_PATH, low_memory=False)

venv/
__pycache__/
*.pyc
.env

# Large dataset
data/survey_results_public.csv

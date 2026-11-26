from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "survey_results_public.csv"
SAMPLE_PATH = DATA_DIR / "survey_sample.csv"


def load_data():
    """Load the full survey dataset, or the sample if the full file is missing."""
    path = DATASET_PATH if DATASET_PATH.exists() else SAMPLE_PATH

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH} "
            f"(sample also missing: {SAMPLE_PATH})"
        )

    return pd.read_csv(path, low_memory=False)
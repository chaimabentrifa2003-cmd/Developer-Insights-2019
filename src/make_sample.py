from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SOURCE_PATH = DATA_DIR / "survey_results_public.csv"
SAMPLE_PATH = DATA_DIR / "survey_sample.csv"

SAMPLE_SIZE = 5000
RANDOM_STATE = 42


def make_sample():
    """Create a reproducible sample of the survey dataset."""
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Full dataset not found: {SOURCE_PATH}")

    df = pd.read_csv(SOURCE_PATH, low_memory=False)
    sample = df.sample(n=SAMPLE_SIZE, random_state=RANDOM_STATE)
    sample.to_csv(SAMPLE_PATH, index=False)
    print(f"Sample saved: {SAMPLE_PATH} ({len(sample)} rows)")


if __name__ == "__main__":
    make_sample()
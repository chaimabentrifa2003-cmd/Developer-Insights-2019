import pandas as pd

from src.eda import dataset_shape, missing_summary


def sample_df():
    return pd.DataFrame({"a": [1, None, 3], "b": ["x", "y", None]})


def test_dataset_shape():
    assert dataset_shape(sample_df()) == (3, 2)


def test_missing_summary_counts():
    summary = missing_summary(sample_df())
    assert summary.loc["a", "missing"] == 1
    assert summary.loc["b", "missing"] == 1

import pandas as pd


def dataset_shape(df: pd.DataFrame) -> tuple:
    """Number of rows and columns."""
    return df.shape


def column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Data type of each column."""
    return df.dtypes.astype(str).rename("dtype").to_frame()


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Descriptive statistics for numeric columns."""
    return df.describe().T

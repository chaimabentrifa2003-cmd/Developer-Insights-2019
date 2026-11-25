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


MAIN_CATEGORICAL = ["MainBranch", "Employment", "EdLevel", "Country", "Gender"]


def categorical_counts(df: pd.DataFrame, columns=None, top: int = 10) -> dict:
    """Top value counts for the main categorical columns."""
    columns = columns or MAIN_CATEGORICAL
    return {
        col: df[col].value_counts(dropna=False).head(top)
        for col in columns
        if col in df.columns
    }

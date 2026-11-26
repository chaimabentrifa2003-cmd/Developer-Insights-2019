import pandas as pd

RELEVANT_COLUMNS = [
    "Respondent",
    "MainBranch",
    "Age",
    "Country",
    "EdLevel",
    "DevType",
    "YearsCode",
    "YearsCodePro",
    "WorkWeekHrs",
    "ConvertedComp",
    "LanguageWorkedWith",
    "LanguageDesireNextYear",
    "DatabaseWorkedWith",
]


def select_relevant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only the columns used in the analysis."""
    columns = [col for col in RELEVANT_COLUMNS if col in df.columns]
    return df[columns].copy()


YEARS_MAPPING = {"Less than 1 year": 0.5, "More than 50 years": 51}


def convert_years_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert YearsCode and YearsCodePro to numeric values."""
    df = df.copy()
    for col in ["YearsCode", "YearsCodePro"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].replace(YEARS_MAPPING), errors="coerce")
    return df

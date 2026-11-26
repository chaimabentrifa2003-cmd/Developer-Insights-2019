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


def normalize_age_and_hours(df: pd.DataFrame) -> pd.DataFrame:
    """Set unrealistic Age and WorkWeekHrs values to missing."""
    df = df.copy()
    if "Age" in df.columns:
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        df.loc[(df["Age"] < 10) | (df["Age"] > 100), "Age"] = pd.NA
    if "WorkWeekHrs" in df.columns:
        df["WorkWeekHrs"] = pd.to_numeric(df["WorkWeekHrs"], errors="coerce")
        df.loc[(df["WorkWeekHrs"] <= 0) | (df["WorkWeekHrs"] > 100), "WorkWeekHrs"] = pd.NA
    return df

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

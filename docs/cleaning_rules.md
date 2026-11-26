# Cleaning rules for columns

- Only the columns listed in `RELEVANT_COLUMNS` (`src/cleaning.py`) are kept.
- `YearsCode` and `YearsCodePro`: "Less than 1 year" becomes 0.5 and "More than 50 years" becomes 51, then the columns are converted to numbers.
- `Age`: values below 10 or above 100 are set to missing.
- `WorkWeekHrs`: values of 0 or less, or above 100, are set to missing.
- Rows are not deleted at this stage, only invalid values become missing.

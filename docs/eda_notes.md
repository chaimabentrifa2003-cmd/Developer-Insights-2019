# Data exploration notes

- Functions are in `src/eda.py`: `dataset_shape`, `column_types`, `numeric_summary`, `categorical_counts`.
- The dataset is the Stack Overflow Developer Survey 2019 (one row per respondent).
- Main numeric columns: `ConvertedComp`, `CompTotal`, `WorkWeekHrs`, `CodeRevHrs`.
- Many columns contain missing values (see the missing values analysis).
- Multi-value columns (e.g. `LanguageWorkedWith`) use `;` as separator and need splitting.

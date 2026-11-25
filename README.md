
# Developer Insights 2019

Interactive dashboard for Stack Overflow Developer Survey 2019.

## Project Description

Developer Insights 2019 is a Business Intelligence project
based on the Stack Overflow Developer Survey 2019.

The objective is to explore developer profiles, programming
languages, professional experience, salaries and technologies.

## Technologies

- Python
- Pandas
- NumPy
- Streamlit
- Plotly

## Project Structure

```text
Developer-Insights-2019/
│
├── data/
│   ├── survey_results_public.csv
│   └── survey_results_schema.csv
│
├── src/
│   ├── __init__.py
│   └── data_loader.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset Setup

Download the Stack Overflow Developer Survey 2019 dataset.

Place the file `survey_results_public.csv` inside the `data/` directory.

The large public dataset is excluded from Git using `.gitignore`.

The schema file is included in the repository.

## Data Loading

The module `src/data_loader.py` provides the
`load_data()` function to load the survey dataset
using Pandas.

## Project Status

- [x] Project structure
- [x] Dependencies configuration
- [x] Dataset schema
- [x] Data loading module
- [ ] Data exploration
- [ ] Data cleaning
- [ ] Interactive dashboard
- [ ] Data validation
## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch and commit conventions.

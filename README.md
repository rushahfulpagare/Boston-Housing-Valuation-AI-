# Boston Housing Valuation AI

An interactive real-time property valuation dashboard built with Streamlit, powered by a trained machine learning model on the Boston Housing dataset.

## Features

- Automated Valuation Model (AVM) with live price prediction
- Projected rental yield, cap rate & 5-year appreciation estimates
- Neighborhood livability scores (Transit, School, Air Quality)
- Interactive visualizations: Radar Profile, Market Delta Benchmark, Valuation Gauge
- Heuristic fallback mode when model artifacts are unavailable

## Project Structure

```
project-2/
├── app.py                        # Main Streamlit application
├── model.joblib                  # Trained ML model
├── scaler.joblib                 # Feature scaler
├── multiple_linear_reg.ipynb     # Model training notebook
├── bostonhousePrice.csv          # Dataset
├── requirements.txt              # Python dependencies
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Input Features

| Feature  | Description                              |
|----------|------------------------------------------|
| CRIM     | Per capita crime rate                    |
| ZN       | Residential land zoned > 25k sq ft (%)  |
| INDUS    | Non-retail business acres (%)            |
| CHAS     | Charles River waterfront (0/1)           |
| NOX      | Nitric oxide concentration (ppm)         |
| RM       | Average rooms per dwelling               |
| AGE      | Units built pre-1940 (%)                 |
| DIS      | Distance to employment hubs              |
| RAD      | Highway accessibility index              |
| TAX      | Property tax rate per $10k               |
| PTRATIO  | Pupil-teacher ratio                      |
| B        | Demographic inclusion index              |
| LSTAT    | Lower income demographics (%)            |

## Model

Trained using scikit-learn on the Boston Housing dataset. Place `model.joblib` and `scaler.joblib` in the project root for live inference. Without them, the app runs in heuristic simulation mode.

# Retail Sales Forecasting & Analytics Dashboard

## Project Overview

This project focuses on forecasting retail sales using time series analysis and machine learning techniques.

The objective is to predict future unit sales using:
- historical sales patterns
- calendar information
- lag-based features
- rolling statistics
- holiday indicators
- external economic variables

The project combines:
- statistical time series analysis
- machine learning forecasting
- HyperOpt hyperparameter optimization
- MLflow experiment tracking
- Streamlit interactive dashboard development

---

## Business Problem

Retail businesses rely on accurate sales forecasting to:
- improve inventory management
- reduce stock shortages
- avoid overstocking
- support operational planning
- improve business decision-making

This project aims to build a forecasting system capable of modeling sales behavior and predicting future demand patterns.

---

## Dataset

The dataset contains retail time series information including:

- Daily unit sales
- Calendar and date features
- Holiday information
- Oil price data
- Lag variables
- Rolling averages and rolling standard deviations

### Target Variable

```text
unit_sales
```

---

## Project Workflow

### Week 1 — Data Cleaning and Exploratory Data Analysis (EDA)

Main tasks:
- loaded and merged datasets
- handled missing values
- cleaned and transformed data
- performed exploratory data analysis
- engineered time-series features
- created lag and rolling statistics
- exported model-ready dataset

---

### Week 2 — Statistical Time Series Analysis

Main tasks:
- stationarity testing using ADF and KPSS
- decomposition analysis
- trend and seasonality analysis
- autocorrelation analysis using ACF/PACF
- baseline forecasting
- statistical forecasting interpretation

---

### Week 3 — Machine Learning Forecasting

Main tasks:
- trained forecasting models
- optimized hyperparameters using HyperOpt
- tracked experiments using MLflow
- evaluated models using forecasting metrics
- selected the best-performing model

### Models Tested

- Ridge Regression
- Random Forest
- Gradient Boosting
- XGBoost

---

### Week 4 — Streamlit Dashboard and Project Presentation

Main tasks:
- developed interactive forecasting dashboard
- visualized forecasting results
- compared model performance
- displayed feature importance
- summarized business insights
- organized GitHub repository

---

## Best Model

### Tuned Ridge Regression

### Performance Metrics

| Metric | Value |
|---|---|
| MAE | 75.93 |
| RMSE | 94.25 |
| MAPE | 19.69% |
| R² | 0.651 |

---

## Dashboard Features

The Streamlit dashboard includes:

- Best model summary
- Forecasting performance metrics
- RMSE comparison across models
- Actual vs predicted sales visualization
- Feature importance visualization
- Downloadable prediction results
- Business insights summary

---

## Key Insights

- Weekend sales consistently exceed weekday sales.
- Lag-based features strongly improve forecasting performance.
- Seasonal and calendar-related effects significantly influence retail demand.
- Historical sales patterns are highly predictive of future sales behavior.
- Forecasting supports better inventory planning and operational decisions.

---

## Repository Structure

```text
retail-sales-forecasting/
│
├── app.py
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── W1_Cleaning_EDA_Project.ipynb
│   ├── W2_Statistical_Time_Series_Analysis_FIXED.ipynb
│   └── W3_Machine_Learning_Forecasting_FROM_SCRATCH.ipynb
│
├── data/
│   └── week1_model_ready.csv
│
├── outputs/
│   ├── week3_tuned_model_comparison.csv
│   ├── week3_best_model_predictions.csv
│   ├── week3_feature_importance.csv
│   ├── week3_best_model_metrics.json
│   └── week3_best_model_name.txt
│
├── models/
│   └── week3_best_model.joblib
│
└── screenshots/
    ├── dashboard_overview.png
    ├── model_comparison.png
    ├── forecast_plot.png
    └── feature_importance.png
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Scikit-learn
- XGBoost
- HyperOpt
- MLflow
- Streamlit
- Plotly

---

## How to Run the Dashboard

### Install required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit dashboard

```bash
streamlit run app.py
```

---

## Dashboard Preview

Add screenshots of:
- dashboard overview
- model comparison
- forecast visualization
- feature importance

inside the `screenshots/` folder.

---

## Conclusion

This project demonstrates an end-to-end retail forecasting workflow combining:
- time series analysis
- machine learning forecasting
- model optimization
- experiment tracking
- interactive dashboard development

The final solution provides both predictive capabilities and business insights for retail demand forecasting.

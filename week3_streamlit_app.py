
import os
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Unit Sales Forecasting', layout='wide')
st.title('Unit Sales Forecasting — Week 3 Prototype')

DATA_DIR = os.path.dirname(__file__)
model_path = os.path.join(DATA_DIR, 'week3_best_model.joblib')
data_path = os.path.join(DATA_DIR, 'week1_model_ready.csv')
results_path = os.path.join(DATA_DIR, 'week3_model_comparison.csv')

st.write('This simple dashboard loads the best Week 3 model and shows model results.')

if os.path.exists(results_path):
    results = pd.read_csv(results_path)
    st.subheader('Model comparison')
    st.dataframe(results)
else:
    st.warning('Model comparison file not found.')

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.subheader('Recent data')
    st.dataframe(df.tail(10))
else:
    st.warning('Model-ready data file not found.')

if os.path.exists(model_path):
    saved = joblib.load(model_path)
    st.success(f"Loaded model: {saved.get('model_name', 'Unknown')}")
else:
    st.warning('Best model file not found.')

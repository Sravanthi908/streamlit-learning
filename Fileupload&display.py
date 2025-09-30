import streamlit as st
import pandas as pd

st.title("📂 Upload CSV Example")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(df.head())

    st.write("Summary Stats:")
    st.write(df.describe())

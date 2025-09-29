import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Input", "Charts"])

if page == "Home":
    st.header("🏠 Home Page")
    st.write("Welcome to the Home page!")

elif page == "Data Input":
    st.header("✍️ Enter Your Data")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=100)
    if st.button("Submit"):
        st.success(f"Hello {name}, you are {age} years old!")

elif page == "Charts":
    st.header("📊 Charts Example")
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(df)
    st.bar_chart(df)


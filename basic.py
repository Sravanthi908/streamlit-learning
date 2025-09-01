import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and subtitle
st.title("🌟 Streamlit Basics Demo")
st.subheader("All-in-one basic example")

# Text and Markdown
st.write("This is a basic **Streamlit** app showing common features.")
st.markdown("### 🔹 Text, Widgets, Charts, and Layouts in one place")

# Input widgets
name = st.text_input("Enter your name")
age = st.slider("Select your age", 1, 100, 25)
hobby = st.selectbox("Select a hobby", ["Coding", "Reading", "Music", "Sports"])

if st.button("Submit"):
    st.success(f"Hello {name}, Age {age}, Hobby: {hobby}")

# Checkbox
if st.checkbox("Show extra message"):
    st.info("You checked the box!")

# Radio buttons
gender = st.radio("Select Gender:", ["Male", "Female", "Other"])
st.write("You selected:", gender)

# File uploader
file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.head())

# Example dataframe
data = pd.DataFrame({
    "A": np.random.randn(10),
    "B": np.random.rand(10),
    "C": np.arange(10)
})
st.write("### Example DataFrame")
st.dataframe(data)

# Charts
st.write("### Line Chart")
st.line_chart(data[["A", "B"]])

st.write("### Bar Chart")
st.bar_chart(data[["C"]])

# Matplotlib chart
fig, ax = plt.subplots()
ax.hist(data["A"], bins=5, color="skyblue", edgecolor="black")
st.pyplot(fig)

# Images
st.write("### Image Example")
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

# Layout with columns
col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")

# Sidebar
st.sidebar.title("Sidebar Menu")
st.sidebar.info("You can put filters, navigation, or extra info here.")

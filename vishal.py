import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("📊 Simple Data Explorer")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Show dataframe
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    # Show basic stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Select column for plotting
    st.subheader("Plot Histogram")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if numeric_cols:
        selected_col = st.selectbox("Select numeric column to plot", numeric_cols)
        fig, ax = plt.subplots()
        df[selected_col].hist(bins=20, ax=ax)
        ax.set_title(f"Histogram of {selected_col}")
        st.pyplot(fig)
    else:
        st.warning("No numeric columns available for plotting.")
else:
    st.info("Please upload a CSV file to get started.")

import streamlit as st
import pandas as pd

st.title("📂 DataFrame Viewer")
st.write("Upload a CSV file and interact with its content.")

# Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Load and Display
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📊 Full Dataset")
    st.dataframe(df)

    # Show raw data
    if st.checkbox("Show raw data"):
        st.write(df)

    # Filter by a column
    if df.shape[1] >= 5:
        column_to_filter = st.selectbox("Select a column to filter by:", df.columns)
        unique_values = df[column_to_filter].dropna().unique()
        selected_value = st.selectbox(f"Select a value from {column_to_filter}:", unique_values)

        filtered_df = df[df[column_to_filter] == selected_value]
        st.subheader("🔍 Filtered Data")
        st.dataframe(filtered_df)
    else:
        st.warning("CSV must contain at least 5 columns.")
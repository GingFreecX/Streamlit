import streamlit as st
import pandas as pd

# Sidebar for filters
st.sidebar.title("Filter Options")
selected_topic = st.sidebar.selectbox("Choose a topic:", ["Data Warehousing", "Enterprise Data Management"])
show_summary = st.sidebar.checkbox("Show Summary", value=True)

st.title("Data Warehousing & Enterprise Data Management")

# Tabs to organize sections
tab1, tab2 = st.tabs(["Overview", "Details"])

with tab1:
    st.header(f"{selected_topic} Overview")

    if selected_topic == "Data Warehousing":
        st.write("A data warehouse is a centralized repository for integrated data from various sources.")
        st.write("It supports analytical reporting, structured queries, and decision making.")
    else:
        st.write("Enterprise Data Management (EDM) refers to the practices, processes, and tools used to manage enterprise data effectively.")
        st.write("It ensures data accuracy, consistency, and governance across the organization.")

with tab2:
    # Columns layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Key Features")
        if selected_topic == "Data Warehousing":
            st.write("- Centralized data storage")
            st.write("- Historical data analysis")
            st.write("- ETL processes (Extract, Transform, Load)")
        else:
            st.write("- Master data management")
            st.write("- Data governance")
            st.write("- Metadata management")

    with col2:
        st.subheader("Benefits")
        if selected_topic == "Data Warehousing":
            st.write("- Improved decision making")
            st.write("- Faster query performance")
            st.write("- Data consistency")
        else:
            st.write("- Better data quality")
            st.write("- Regulatory compliance")
            st.write("- Cross-functional alignment")

# Expander section for additional details
with st.expander("Click to view additional insights"):
    if selected_topic == "Data Warehousing":
        st.write("Data warehouses often use star or snowflake schemas and are optimized for read-heavy workloads.")
    else:
        st.write("EDM involves setting up data stewardship roles and ensuring compliance with data privacy regulations.")

# Optional summary
if show_summary:
    st.sidebar.subheader("Summary")
    st.sidebar.write(f"You selected: {selected_topic}")

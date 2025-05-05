import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ------------------ AUTH SECTION ------------------ #
# Hardcoded credentials (for demo)
USER_CREDENTIALS = {"admin": "1234", "manager": "abcd"}

# Auth form
with st.sidebar:
    st.header("🔒 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.button("Login")

# Authentication check
if login:
    if USER_CREDENTIALS.get(username) == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success(f"Welcome, {username}!")
    else:
        st.error("Invalid credentials")
        st.stop()

# If not logged in, stop the execution
if not st.session_state.get("logged_in", False):
    st.stop()
# --------------------------------------------------- #

# Database connection
try:
    engine = create_engine("mysql+mysqlconnector://root@localhost/company")
    conn = engine.connect()
    st.sidebar.success("✅ Connected to MySQL")
except Exception as e:
    st.sidebar.error(f"❌ DB Connection Failed: {e}")
    st.stop()

st.title("🗂️ Company Employee Database")

# --- Insert New Employee --- #
with st.expander("➕ Add New Employee"):
    with st.form("employee_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        dept = st.selectbox("Department", ["HR", "IT", "Sales", "Finance"])
        salary = st.number_input("Salary", min_value=0.0, step=100.0)
        submit = st.form_submit_button("Insert")

        if submit:
            insert_query = text("INSERT INTO employees (name, department, salary) VALUES (:n, :d, :s)")
            conn.execute(insert_query, {"n": name, "d": dept, "s": salary})
            conn.commit()
            st.success("✅ Employee added successfully!")

# --- Filter and Display Data --- #
st.subheader("📊 View Employee Records")

dept_filter = st.sidebar.selectbox("Filter by Department", ["All", "HR", "IT", "Sales", "Finance"])
if dept_filter == "All":
    query = "SELECT * FROM employees"
else:
    query = text("SELECT * FROM employees WHERE department = :dept")

try:
    if dept_filter == "All":
        df = pd.read_sql("SELECT * FROM employees", conn)
    else:
        df = pd.read_sql(query, conn, params={"dept": dept_filter})

    st.dataframe(df)
except Exception as e:
    st.error(f"Failed to fetch data: {e}")
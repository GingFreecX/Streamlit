import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("COVID-19 Statistics Dashboard")

# Get country selection
country = st.selectbox("Select a country", ["USA", "India", "Brazil", "France", "Russia"])

# Fetch data from COVID-19 API
url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
response = requests.get(url)
data = response.json()

if 'timeline' in data:
    cases = data['timeline']['cases']
    deaths = data['timeline']['deaths']
    recovered = data['timeline']['recovered']

    # Convert to DataFrame
    df = pd.DataFrame({
        'Date': pd.to_datetime(list(cases.keys())),
        'Cases': list(cases.values()),
        'Deaths': list(deaths.values()),
        'Recovered': list(recovered.values())
    })

    st.subheader(f"COVID-19 Last 30 Days in {country}")
    st.dataframe(df)

    # Line Chart
    st.subheader("Line Chart (Cases Over Time)")
    st.line_chart(df.set_index('Date')['Cases'])

    # Bar Chart
    st.subheader("Bar Chart (Deaths Over Time)")
    st.bar_chart(df.set_index('Date')['Deaths'])

    # Area Chart
    st.subheader("Area Chart (Recovered Over Time)")
    st.area_chart(df.set_index('Date')['Recovered'])

    # Pie Chart (Today’s Share)
    st.subheader("Pie Chart (Current Distribution)")
    today_url = f"https://disease.sh/v3/covid-19/countries/{country}"
    today_data = requests.get(today_url).json()
    pie_df = pd.DataFrame({
        'Category': ['Active', 'Recovered', 'Deaths'],
        'Count': [today_data['active'], today_data['recovered'], today_data['deaths']]
    })
    fig_pie = px.pie(pie_df, names='Category', values='Count', title='Current Cases Breakdown')
    st.plotly_chart(fig_pie)

    # Scatter Plot
    st.subheader("Scatter Plot (Cases vs Deaths)")
    fig_scatter = px.scatter(df, x='Cases', y='Deaths', title='Cases vs Deaths Over Time')
    st.plotly_chart(fig_scatter)

else:
    st.error("Data not available for the selected country.")

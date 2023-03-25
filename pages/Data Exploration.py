import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta, date
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")
st.title("Our Data")
st.header("On this page, we will consider how we explored our dataset and how that led to our dashboard!")

st.write("Below is the top 20 rows of one of our datasets: ")
df = yf.download("AAPL", start="2021-01-01", end=date.today())
st.write(df.head(20))

st.write("The data above is just the ticker for Apple. Instead of specifically being apple, our app takes in your input and retrieves the necessary data for that.")

st.write("Furthermore, our app is customized to choose between the New York Stock Exchange or National Associaton of Securities Dealers Automated Quotations.")
st.write("For example, Apple is part of NASDAQ, while a company like JP Morgan Chase is part of the NYSE. This adds another layer of customization within our app.")
st.write("The user also slices the data by choosing a start and an end date.")

st.write("Once the user enters all of their input, the dashboard shows 3 visuals:")
st.write("1) A graph showing volume of stocks over time")
st.write("2) A graph showing open and close values of stocks over time")
st.write("3) A graph showing high and low values of stocks over time")

st.write("Furthermore, our graph shows the change in open, close, high, low, and volume values over the given interval below the visuals")

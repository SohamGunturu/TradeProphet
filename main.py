import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta, date

# st.set_page_config(layout="wide")
st.title('Trade Prophet')
st.markdown('This app built with Streamlit would give you the performance of the stocks today.')
# Create the container

sidebar = st.container()
dfset = st.container()
open_close = st.container()
high_low = st.container()
volume = st.container()
change = st.container()

# Sidebar
with sidebar:
    st.sidebar.title('Options')
    market = st.sidebar.selectbox('Enter Market', np.array(['NYSE', 'NASDAQ']))
    if market == 'NYSE':
        ticker = st.sidebar.selectbox('Enter Ticker', ('C', 'JPM', 'WFC', 'BAC')   )
    elif market == 'NASDAQ':
        ticker = st.sidebar.selectbox('Enter Ticker', ('AAPL', 'MSFT', 'GOOG', 'AMZN', 'FB', 'GOOG', 'AMD'))
    start = st.sidebar.date_input('Enter Start Date', date.today() - timedelta(days=100))
    end = st.sidebar.date_input('Enter End Date', date.today())

# dfset
df = yf.download(ticker, start=start, end=end)
df = df[::-1]

# Volume
with volume:
    fig_vol = px.area(df, x=df.index, y="Volume", title='Volume')
    st.plotly_chart(fig_vol)

# Open Close
with open_close:
    fig_oc = px.line(df, x = df.index, y = ["Open", "Close"], title = "Open - Close")
    st.plotly_chart(fig_oc)

# High Low
with high_low:
    fig_hl = px.line(df, x = df.index, y = ["High", "Low"], title = "High - Low")
    st.plotly_chart(fig_hl)

# Change

with change:

    # Data for current day
    close_now = round(float(str(df.head(1)['Close'].values[0])), 2)
    open_now = round(float(str(df.head(1)['Open'].values[0])), 2)
    high_now = round(float(str(df.head(1)['High'].values[0])), 2)
    low_now = round(float(str(df.head(1)['Low'].values[0])), 2)

    # Data for the first day on the dataset
    close_past = round(float(str(df.tail(1)['Close'].values[0])), 2)
    open_past = round(float(str(df.tail(1)['Open'].values[0])), 2)
    high_past = round(float(str(df.tail(1)['High'].values[0])), 2)
    low_past = round(float(str(df.tail(1)['Low'].values[0])), 2)

    # Change in the price
    close_change = round(close_now - close_past, 2)
    open_change = round(open_now - open_past, 2)
    high_change = round(high_now - high_past, 2)
    low_change = round(low_now - low_past, 2)

    # Change in percentage based on the first day
    close_percent = round(close_change / close_past * 100, 2)
    open_percent = round(open_change / open_past * 100, 2)
    high_percent = round(high_change / high_past * 100, 2)
    low_percent = round(low_change / low_past * 100)

    # Open and Close
    col1, col2 = st.columns(2)
    col1.metric('Close', str(close_now), str(close_change) +' (' + str(close_percent) + '%)')
    col2.metric('Open', str(open_now), str(open_change) + ' (' + str(open_percent) + '%)')

    # High and Low
    col3, col4 = st.columns(2)
    col3.metric('High', str(high_now), str(high_change) + ' (' + str(high_percent) + '%)')
    col4.metric('Low', str(low_now), str(low_change) +'(' + str(low_percent) + '%)')

    # Hi
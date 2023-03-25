import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta, date

# st.set_page_config(layout="wide")
st.title('Trade Prophet')

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
        ticker = st.sidebar.selectbox('Enter Ticker', ('AAPL', 'MSFT', 'GOOG', 'AMZN', 'FB', 'GOOG'))
    start = st.sidebar.date_input('Enter Start Date', date.today() - timedelta(days=100))
    end = st.sidebar.date_input('Enter End Date')

# dfset
df = yf.download(ticker, start=start, end=end)

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
    close_now = round(float(str(df.tail(1)['Close'].values[0])), 2)
    open_now = round(float(str(df.tail(1)['Open'].values[0])), 2)
    high_now = round(float(str(df.tail(1)['High'].values[0])), 2)
    low_now = round(float(str(df.tail(1)['Low'].values[0])), 2)

    close_past = round(float(str(df.head(1)['Close'].values[0])), 2)
    open_past = round(float(str(df.head(1)['Open'].values[0])), 2)
    high_past = round(float(str(df.head(1)['High'].values[0])), 2)
    low_past = round(float(str(df.head(1)['Low'].values[0])), 2)
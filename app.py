import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta, date

st.set_page_config(layout="wide")
st.title('Trade Prophet')

# Create the container

sidebar = st.container()
dataset = st.container()
open_close = st.container()
high_low = st.container()
volume = st.container()


# Sidebar
with sidebar:
    st.sidebar.title('Options')
    market = st.sidebar.selectbox('Enter Market', np.array(['NYSE', 'NASDAQ']))
    if market == 'NYSE':
        ticker = st.sidebar.selectbox('Enter Ticker', ('C', 'JPM', 'WFC', 'BAC')   )
    elif market == 'NASDAQ':
        ticker = st.sidebar.selectbox('Enter Ticker', ('AAPL', 'MSFT', 'GOOG', 'AMZN', 'FB', 'GOOG'))
    start = st.sidebar.date_input('Enter Start Date', date.today() - timedelta(days=365))
    end = st.sidebar.date_input('Enter End Date')

# Dataset
df = yf.download(ticker, start=start, end=end)

with volume:
    fig_vol = px.area(df, x=df.index, y="Volume", title='Volume')
    st.plotly_chart(fig_vol)

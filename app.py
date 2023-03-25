import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.title('Trade Prophet')

# Create the container

sidebar = st.container()

# 
with sidebar:
    st.sidebar.title('Options')
    st.sidebar.selectbox('Enter Market', np.array(['NYSE', 'NASDAQ']))
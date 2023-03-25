import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

st.set_page_config(layout = "wide")
st.title("Our Data")
st.header("On this page, we will consider how we explored our dataset and how that led to our dashboard!")

st.write("Below is the top 20 rows of one of our datasets: ")
df = yf.download("AAPL", start="2021-01-01", end=date.today())
st.write(df.head(20))

st.write("The data above is just the ticker for Apple. Instead of specifically being apple, our app takes in your input and retrieves the necessary data for that.")

st.write("Furthermore, our app is customized to choose between the New York Stock Exchange or National Associaton of Securities Dealers Automated Quotations. For example, Apple is part of NASDAQ, while a company like JP Morgan Chase is part of the NYSE. This adds another layer of customization within our app. The user also slices the data by choosing a start and an end date.")

st.write("Once the user enters all of their input, the dashboard shows 3 visuals:")
st.write("1) A graph showing volume of stocks over time")
st.write("2) A graph showing open and close values of stocks over time")
st.write("3) A graph showing high and low values of stocks over time")

st.write("Furthermore, our graph shows the change in open, close, high, low, and volume values over the given interval below the visuals")
st.header('Machine Learning Algorithm')
st.write('In the dataset the close price is shifted based on the days the user wants to see. So for example, if you use the slider and select 10 days the closing price would be shifted by 10 days and it would be saved in the **prediction** column. Next, we would use that to predict the close price using the random forest regressor model. For that the dataset would be split into 80% train and 20% test sets. Then the model would predict the close price for the 10 days after the 10 days of the train set. Finally, the score would be based on how well the model predicts the close price for the 10 days.')

future_days = 100
st.header('Implementation')
data = yf.download('AAPL', start=date.today() - relativedelta(days=future_days * 100), end=date.today())
data['Prediction'] = data['Close'].shift(-future_days)
X = np.array(data.drop(columns=['Prediction'], axis=1))[:-future_days]
y = np.array(data['Prediction'])[:-future_days]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#model = RandomForestRegressor(n_estimators=10, max_depth=10)
model = DecisionTreeRegressor(max_depth=20, random_state=2)
x_future = data.drop(columns=['Prediction'], axis=1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
model.fit(x_train, y_train)
forest_prediction = model.predict(x_future)
predictions = forest_prediction
valid = data[X.shape[0]:].copy()
valid['Prediction'] = predictions
valid.drop(columns=['Prediction'], axis=1)
# print(valid.head())
predict_graph = px.line(valid, x=valid.index, y=['Close', 'Prediction'])
predict_graph.update_layout(title='Close vs Prediction', xaxis_title='Date', yaxis_title='Price')
st.plotly_chart(predict_graph)

score = str(float(round(model.score(x_test, y_test) * 100, 2)))
st.subheader('Model Score: ' + score + '%')

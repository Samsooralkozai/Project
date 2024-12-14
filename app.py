import streamlit as st
import plotly.express as px
import pandas as pd

# Load and clean the dataset
df = pd.read_csv("./data/vehicles_us.csv")
df_cleaned = df.dropna()

# Header for the dashboard
st.header("Car Sales Analysis Dashboard")

# Interactive checkbox to filter by condition
show_cleaned = st.checkbox("Show only cleaned data (no missing values)")

# Use filtered or unfiltered data
data_to_use = df_cleaned if show_cleaned else df

# Distribution of model years
st.subheader("Distribution of Model Years")
fig_model_year = px.histogram(data_to_use, x='model_year', title='Distribution of Model Years')
st.plotly_chart(fig_model_year)

# Distribution of prices
st.subheader("Distribution of Prices")
fig_prices = px.histogram(data_to_use, x='price', title='Distribution of Prices')
st.plotly_chart(fig_prices)

# Price vs odometer scatter plot
st.subheader("Price vs Odometer")
fig_odometer = px.scatter(data_to_use, x='odometer', y='price', title='Price vs Odometer', trendline='ols')
st.plotly_chart(fig_odometer)

# Vehicle types by paint color
st.subheader("Vehicle Types by Paint Color")
fig_vehicle_types = px.histogram(data_to_use, x='type', color='paint_color', title='Vehicle Types by Paint Color')
st.plotly_chart(fig_vehicle_types)

# Vehicle condition counts
st.subheader("Vehicle Condition Counts")
condition_counts = data_to_use['condition'].value_counts().reset_index()
condition_counts.columns = ['condition', 'count']
fig_condition = px.bar(condition_counts, x='condition', y='count', title='Vehicle Condition Counts')
st.plotly_chart(fig_condition)

# Average price by fuel type
st.subheader("Average Price by Fuel Type")
average_price_fuel = data_to_use.groupby('fuel')['price'].mean().reset_index()
fig_fuel_price = px.bar(average_price_fuel, x='fuel', y='price', title='Average Price by Fuel Type')
st.plotly_chart(fig_fuel_price)

import streamlit as st
import plotly.express as px
import pandas as pd


# load and clean the dataset
df = pd.read_csv("./data/vehicles_us.csv")
df_cleaned = df.dropna()

# Plot the data
fig = px.histogram(df, x='model_year', title='Distribution of Model Years')
st.plotly_chart(fig)

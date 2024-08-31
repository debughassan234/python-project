import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt



st.title('Aircrashes from 1908-2024')
st.text('This application is a Streamlit dashboard hosted on the Streamlit cloud server that can be used to analyze Aircrashes from 1908-2024')



st.header('Aircrash Dataset')
st.text('I found this dataset on Kaggle')

Aircrash_data = data = pd.read_csv("C:\\Users\\dell\\Desktop\\NewAircrash.xlsx")
st.write(Aircrash_data.head())

# -1 Arcrashes by the year
st.title('Aircrashes by year')
x = st.slider ('1904-2024', min_value=1904, max_value=2024)
st.text('The number of crashes gradually increased from 1908')
st.text('Till 1943 the accidents were only confined to 40 or less than that')
st.text('After 1944 and upto the  2005 number rapidly increased which were greater than 40 and almost near to 80 crashes')
st.text('From 1945 the number increases much more and each year minimum of 60 crashes sarted talking place and the number went till 80')
st.text('After the advancement of auto-pilot some other major innovations of the air craft, the number started decreasing after year 2000, but upto 2008 there were minimum of 50 crashes happening')
st.text('the years 2005, 2006, 2007, 2009 had minimum of 40 crashes')
st.text('After 2009, The numbers are drastically low, because of the capabilities of the modern aircraft')

crashes_per_month = data.groupby('Year').size().reset_index(name='Count')

fig = px.bar(crashes_per_month, x='Year', y='Count',
             title='Air Crashes by Year',
             labels={'Year': 'Year', 'Count': 'Number of Crashes'})
fig.update_xaxes(tickangle=100)
st.write(fig)


st.title('Air Crashes by Quater')
data['Quarter'] = data['Year'].astype(str) + 'Q' + data['Quarter']

crashes_per_quarter = data.groupby('Quarter').size().reset_index(name='CrashCount')

fig = px.bar(crashes_per_quarter, x='Quarter', y='CrashCount',
             title='Air Crashes by Quarter',
             labels={'Quarter': 'Quarter', 'CrashCount': 'Number of Crashes'})
fig.update_xaxes(tickangle=125)
st.write(fig)



st.title('Aircrashes by Month')
st.text('December months have more number of crashes with nearly 500 crashes')
st.text('January months have the second highest month with crashes nearly 500')
st.text('March, July, August, September, October, November have more than 400+ crashes')
st.text('February, April, May, June have more than 300+ crashes')

crashes_per_month = data.groupby('Month').size().reset_index(name='Count')

fig = px.bar(crashes_per_month, x='Month', y='Count',
             title='Air Crashes by Month',
             labels={'Month': 'Month', 'Count': 'Number of Crashes'})
fig.update_xaxes(tickangle=45)
st.write(fig)



st.title('AirCrashes Per Region')
st.text('Looking at the number of crashes, Russia as almost 250 crashes')
st.text('It is then followed India, that has 200+ Crashes')
st.text('It is then followed by Brazil, that has 162 crashes')

crashes_per_country = data.groupby('Country/Region').size().reset_index(name='Count')

fig = px.bar(crashes_per_country, x='Country/Region', y='Count',
             title='Country with highest number of Fatalities',
             labels={'Country/Region': 'Country', 'Count': 'Number of Crashes'})
fig.update_xaxes(tickangle=45)
st.write(fig)


st.title('Average Number of Fatalities Per Crash')
st.text('. Average Fatalities per crash resulted into 22.22')

average_fatalities_per_crash = data["Fatalities (air)"].mean()
data = print(f"Average Fatalities per Crash: {average_fatalities_per_crash:.2f}")
st.write(data)
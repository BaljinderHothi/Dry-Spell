import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PURPLEAIR_API_KEY")
SENSOR_INDEX = '138818'

data = {
    "AQI Category": ["Good", "Moderate", "Unhealthy for Sensitive Groups", 
                     "Unhealthy", "Very Unhealthy", "Hazardous"],
    "Index Values": ["0 - 50", "51 - 100", "101 - 150", 
                     "151 - 200", "201 - 300", "301 - 500"],
    "Revised Breakpoints (µg/m³, 24-hour average)": [
        "0.0 – 12.0", "12.1 – 35.4", "35.5 – 55.4", 
        "55.5 – 150.4", "150.5 – 250.4", "250.5 – 500"
    ]
}

# Convert the data into a DataFrame
df2 = pd.DataFrame(data)

@st.cache_data
def load_data():
    file_path = './Data/Water_Consumption_in_the_City_of_New_York_20241109.csv'
    try:
        df = pd.read_csv(file_path)
        df['Total Consumption (Billion gallons per year)'] = df['NYC Consumption(Million gallons per day)'] * 365 / 1e3
        return df
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        return None

def fetch_air_quality(sensor_index):
    url = f"https://api.purpleair.com/v1/sensors/{sensor_index}"
    headers = {
        "X-API-Key": API_KEY
    }
    params = {
        "fields": "pm2.5_atm"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if 'sensor' in data:
            pm25 = data['sensor']['pm2.5_atm']
            return pm25
        else:
            st.error("No air quality data available")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching air quality data: {e}")
        return None


df = load_data()


st.title("Dry Spell")
st.markdown("### Made by Baljinder Hothi and Abrar Habib")

st.write("""
Ask any Native New Yorker when the last time we had a dry spell of no water was? 
Many of them cannot even remember it as we are used to it raining so often in NYC.

What inspired this project was the recent fire in Prospect Park in Brooklyn as well as the advisories to preserve water in NYC. This got us thinking, when was the last time it actually rained in NYC?

The last time it rained in NYC was Sept 27....

It has been 43 days and counting of no rain.
         
Not only is this drought causing us to preserve water, but it's also causing fires and lowering the air quality index.
""")


st.subheader("Latest Air Quality Index for NYC")
air_quality = fetch_air_quality(SENSOR_INDEX)

if air_quality is not None:
    st.write(f"**Current PM2.5 Concentration:** {air_quality} µg/m³")
else:
    st.write("Could not retrieve air quality data at this time.")

st.subheader("Air Quality Index (AQI) Categories")
st.dataframe(df2)

st.write(""" 
             Short-term exposure can cause irritation of the eyes, nose, throat, and lungs. It can also worsen conditions like asthma and heart disease.
              
         Long-term exposure is linked to more severe health problems such as chronic respiratory diseases, lung cancer, and cardiovascular diseases.
             """)

st.subheader("Facts")
st.write("""
- Fact 1: NYC gets an average of 47 inches of rain per year.
- Fact 2: The city’s water supply comes from 19 reservoirs and three controlled lakes.
- Fact 3: Water conservation efforts have reduced daily water usage by over 30% since the 1990s.
""")

if df is not None:
    st.subheader("NYC Water Consumption Data")
    st.dataframe(df)

    # water consumption 
    st.subheader("NYC Water Consumption Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df['NYC Consumption(Million gallons per day)'], marker='o')
    ax.set_title('NYC Water Consumption Over Time (Million Gallons per Day)')
    ax.set_xlabel('Year')
    ax.set_ylabel('NYC Consumption (Million Gallons per Day)')
    ax.grid(True)
    st.pyplot(fig)

    # per Capita Consumption Over Time
    st.subheader("Per Capita Water Consumption Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df['Per Capita(Gallons per person per day)'], marker='o', color='orange')
    ax.set_title('Per Capita Water Consumption Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Per Capita (Gallons per Person per Day)')
    ax.grid(True)
    st.pyplot(fig)

    # total Water Consumption
    st.subheader("Total Water Consumption in NYC (Billion Gallons per Year)")
    fig, ax = plt.subplots()
    ax.bar(df['Year'], df['Total Consumption (Billion gallons per year)'], color='green')
    ax.set_title('Total Water Consumption (Billion Gallons per Year)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Consumption (Billion Gallons per Year)')
    ax.grid(True)
    st.pyplot(fig)

    st.subheader("Key Statistics")
    st.write(df.describe())
else:
    st.error("Data could not be loaded.")

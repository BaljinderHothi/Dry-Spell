import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Load the dataset
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

# Load data
df = load_data()

# Streamlit App Interface
st.title("Dry Spell")
st.markdown("### Made by Baljinder Hothi and Abrar Habib")


st.write("""
Ask any Native New Yorker when the last time we had a dry spell of no water was? 
Many of them cannot even remember it as we are used to it raining so often in NYC.

What inspired this project was the recent fire in Prospect Park in Brooklyn as well as the advisories to preserve water in NYC. This got us thinking, when was the last time it actually rained in NYC?

The last time it rained in NYC was Sept 27....

It has been 43 days and counting of no rain.
         
Not only is this drought causing us to preserve water, but its also causing fires the lower the air quality index.
         
""")

def fetch_air_quality():
    api_url = "https://api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": 40.7128,  # NYC latitude
        "longitude": -74.0060,  # NYC longitude
        "hourly": "pm10,pm2_5,ozone,carbon_monoxide,sulphur_dioxide,nitrogen_dioxide"
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extracting the latest air quality data from the response
        if 'hourly' in data:
            latest_data = {
                "PM10": data["hourly"]["pm10"][-1],
                "PM2.5": data["hourly"]["pm2_5"][-1],
                "Ozone": data["hourly"]["ozone"][-1],
                "CO": data["hourly"]["carbon_monoxide"][-1],
                "SO2": data["hourly"]["sulphur_dioxide"][-1],
                "NO2": data["hourly"]["nitrogen_dioxide"][-1]
            }
            return latest_data
        else:
            st.error("No air quality data available")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching air quality data: {e}")
        return None

st.subheader("Latest Air Quality Index for NYC")
air_quality_data = fetch_air_quality()

if air_quality_data:
    st.write("### Current Air Quality Levels in NYC:")
    for pollutant, level in air_quality_data.items():
        st.write(f"{pollutant}: {level} µg/m³")
else:
    st.write("Could not retrieve air quality data at this time.")

st.subheader("Facts")
st.write("""
- Fact 1: NYC gets an average of 47 inches of rain per year.
- Fact 2: The city’s water supply comes from 19 reservoirs and three controlled lakes.
- Fact 3: Water conservation efforts have reduced daily water usage by over 30% since the 1990s.
""")


st.subheader("Latest Weather ")
st.write("This section will display the latest weather news from API calls.")
st.text("Yap yap yap... (API integration goes here)")

st.subheader("What Does This Drought Mean?")
st.text("Yap yap yap yap yap yap yap yap yap yap... (You can fill in details here)")

st.subheader("What Can We Do?")
st.text("Yap yap yap yap yap yap yap yap yap yap... (You can fill in details here)")



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

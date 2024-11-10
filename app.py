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
st.markdown("### Made by [Baljinder Hothi](https://www.linkedin.com/in/baljinder-hothi/) and [Abrar Habib](https://www.linkedin.com/in/abrar-habib1/)")

st.markdown("""
Check out the [GitHub repository](https://github.com/BaljinderHothi/Dry-Spell) for more details on the project.
""")


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

st.subheader("Water Storage and Consumption (as of November 8, 2024)")
st.markdown("""- **Total Storage Capacity**:
  - Current: **63.6%**
  - Normal: **79.1%**
- **Daily Consumption** (as of 11/07/24): **0.99 billion gallons**
""")

st.subheader("Average Precipitation (inches)")
st.markdown("""
- **September**: 
  - Actual: **1.36** | Historical: **4.72**
- **October**: 
  - Actual: **0.87** | Historical: **4.12**
- **November**: 
  - Actual: **0.00** | Historical: **0.54**
""")

st.subheader("Facts")
st.write("""
- Fact 1: NYC gets an average of 47 inches of rain per year.
- Fact 2: The city’s water supply comes from 19 reservoirs and three controlled lakes.
- Fact 3: Water conservation efforts have reduced daily water usage by over 30% since the 1990s.
- Fact 4: NYC has three main sources of water: The Catskill, Delaware, and Croton Systems      
- Catskill System: Provides up to 40% of daily water;   
- Delaware System: Supplies 50% of daily water; its largest reservoir has a capacity of 140 billion gallons.
- Croton System: Contributes 10% of daily water (more during droughts);  its largest reservoir has a capacity of 19 billion gallons.
""")
st.title("NYC Water Systems")
st.image("water nyc.jpg", caption="Source: NYC Department Of Environmental Protection", use_container_width =True)
if df is not None:
    st.subheader("NYC Water Sources")
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

    st.write("This figure shows the decreasing water consumption in NYC over the past several decades. This could be attributed to factors like improved water conservation measures, or technological advancements in water usage efficiency.")
    
    st.write(" ")
    # per Capita Consumption Over Time
    st.subheader("Per Capita Water Consumption Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df['Per Capita(Gallons per person per day)'], marker='o', color='orange')
    ax.set_title('Per Capita Water Consumption Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Per Capita (Gallons per Person per Day)')
    ax.grid(True)
    st.pyplot(fig)
    st.write("The graph shows a clear decline in per capita water consumption over the decades, likely due to conservation efforts, efficiency improvements, and regulatory measures. This aligns with the overall reduction in NYC’s water usage shown in the previous graph.")

    st.write(" ")
    # total Water Consumption
    st.subheader("Total Water Consumption in NYC (Billion Gallons per Year)")
    fig, ax = plt.subplots()
    ax.bar(df['Year'], df['Total Consumption (Billion gallons per year)'], color='green')
    ax.set_title('Total Water Consumption (Billion Gallons per Year)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Consumption (Billion Gallons per Year)')
    ax.grid(True)
    st.pyplot(fig)
    st.write("The graph shows a significant reduction in NYC's total water consumption over the decades, consistent with earlier charts on daily and per capita usage. This likely reflects efficiency improvements, conservation efforts, and regulatory measures.")

    st.subheader("Conclusion")
    st.write("""
    NYC is currently experiencing a historic drought, with over 40 days without rain—something most New Yorkers have never seen before. This dry spell is affecting us in more ways than just water conservation. It's increasing the risk of fires, degrading air quality, and taking a toll on people's health.

    While our analysis highlights how NYC has managed to cut down water usage over the years, this drought shows we can’t let up on conservation efforts. By digging into historical rainfall trends and monitoring current conditions, we can be better prepared to handle future droughts and protect our water supply and community well-being.
    """)
    st.subheader("Key Statistics")
    st.write(df.describe())
else:
    st.error("Data could not be loaded.")

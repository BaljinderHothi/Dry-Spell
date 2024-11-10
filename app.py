import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
         
         # Display air quality index live below if possible
""")

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

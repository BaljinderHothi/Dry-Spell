# Dry-Spell
### Created by Baljinder Hothi and Abrar Habib (ill link our linkedins later)

If you ask any New York City resident about when was the last time they had over 40 days of no rain, they would't be able to tell you, thats because this is a historic event in New York City. This project aims to discuss the impacts and information around NYC's recent drought conditions, visualize historical rainfall data, and discuss the implications for our water supply.

## 🗝️ Key Features:
Causes of NYC's Current Drought: Analyzing factors contributing to recent dry conditions.
Rainfall Data Visualization: Interactive graphs showcasing changes in rainfall patterns over the years.
Water Consumption Insights: Understanding how NYC's residents use water and the impact on reservoir levels.
Real-Time Weather Updates: Leveraging weather APIs to monitor current conditions and drought alerts.

## 🛠️ Tech Stack

Programming Language: Python

Data Analysis & Visualization: Pandas, Matplotlib, Plotly, Seaborn

APIs: PurpleAir API

Frontend: Streamlit 

Hosting: Streamlit

## 📊 Data Sources

1. **NYC Department of Environmental Protection**: Provides historical data on water consumption, rainfall, and reservoir levels, giving insights into how NYC's water usage has evolved over the decades.
   
3. **PurpleAir API**: Integrated to fetch real-time air quality data, focusing on PM2.5 concentrations to assess the impact of drought conditions on air quality in NYC.

## 🚀 How It Works

1. **Data Loading & Preprocessing**: The app loads historical water consumption data and calculates total water usage per year based on daily consumption rates.

2. **Air Quality Monitoring**:
   - Utilizes the **PurpleAir API** to fetch the latest PM2.5 data using:
     ```python
     import os
     import requests
     API_KEY = os.getenv("PURPLEAIR_API_KEY")
     SENSOR_INDEX = '138818'
     ```
     
   - Displays real-time air quality data, which is crucial given the current drought's impact on health.

3. **Interactive Visualizations**:
   
   - Historical trends in **NYC water consumption** are displayed through line charts, showing both per capita and total water usage over time.
     
   - Bar charts visualize **total annual water consumption**, highlighting reductions due to conservation efforts.
     
   - Real-time data on NYC’s water storage levels and daily consumption figures are shown.

## 🌍 Why This Project Matters

The recent dry spell in NYC is not just a matter of water conservation but also a public health concern. The lack of rainfall has led to fires, reduced air quality, and increased health risks. This project brings awareness to these issues and emphasizes the need for continued efforts in water conservation and air quality monitoring.

By analyzing historical trends and leveraging real-time data, we aim to provide insights that can help policymakers and the public better prepare for the impacts of prolonged droughts.

## 📈 Example Visualizations

1. **NYC Water Consumption Over Time**: 
   - Line chart showing a decline in water usage since the 1990s, attributed to conservation measures and technological advancements.

2. **Per Capita Water Usage**:
   - Illustrates the reduction in per capita consumption, reflecting the success of water-saving initiatives.

3. **Air Quality Index**:
   - Real-time display of the latest air quality readings, categorized by AQI levels to inform residents of health risks.

## 🔗 Additional Links

- **Live Website**: [Dry-Spell](https://dryspell.streamlit.app/)
- **LinkedIn Profiles**:
  - [Baljinder Hothi](https://www.linkedin.com/in/baljinder-hothi/)
  - [Abrar Habib](https://www.linkedin.com/in/abrar-habib1/)

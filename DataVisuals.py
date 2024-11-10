import pandas as pd
import matplotlib.pyplot as plt
file_path = './Data/Water_Consumption_in_the_City_of_New_York_20241109.csv'
df = pd.read_csv(file_path)
df.isnull().sum()
df['Total Consumption (Billion gallons per year)'] = df['NYC Consumption(Million gallons per day)'] * 365 / 1e3

#Water Consumption Over Time
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['NYC Consumption(Million gallons per day)'], marker='o')
plt.title('NYC Water Consumption Over Time (Million Gallons per Day)')
plt.xlabel('Year')
plt.ylabel('NYC Consumption (Million Gallons per Day)')
plt.grid(True)
plt.tight_layout()
plt.show()

#Per Capita Water Consumption Over Time
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Per Capita(Gallons per person per day)'], marker='o', color='orange')
plt.title('NYC Per Capita Water Consumption Over Time (Gallons per Person per Day)')
plt.xlabel('Year')
plt.ylabel('Per Capita Consumption (Gallons per Person per Day)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Population vs Total Consumption
plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Total Consumption (Billion gallons per year)'], color='green')
plt.title('Total Water Consumption in NYC Over Time (Billion Gallons per Year)')
plt.xlabel('Year')
plt.ylabel('Total Consumption (Billion Gallons per Year)')
plt.grid(True)
plt.tight_layout()
plt.show()


print(df.describe())

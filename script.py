# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up seaborn for better plotting
sns.set(style="whitegrid")

# Function to get COVID-19 data from the API
def get_global_data():
    url = 'https://disease.sh/v3/covid-19/all'  # Global data endpoint
    response = requests.get(url)
    data = response.json()
    return data

def get_country_data():
    url = 'https://disease.sh/v3/covid-19/countries'  # Country data endpoint
    response = requests.get(url)
    data = response.json()
    return data

# Fetch global data
global_data = get_global_data()
print("Global COVID-19 Data:")
print(f"Total Cases: {global_data['cases']}")
print(f"Total Deaths: {global_data['deaths']}")
print(f"Total Recovered: {global_data['recovered']}")
print(f"Total Active Cases: {global_data['active']}\n")

# Fetch country-wise data
country_data = get_country_data()

# Convert country data into a Pandas DataFrame
df = pd.DataFrame(country_data)

# Display the first few rows of the country data
print("\nCountry-wise COVID-19 Data (Top 5 countries):")
print(df[['country', 'cases', 'deaths', 'recovered', 'active']].head())

# Plotting: Total Cases vs Total Deaths (for the top 10 countries)
top_10_countries = df.nlargest(10, 'cases')

plt.figure(figsize=(12, 6))
plt.barh(top_10_countries['country'], top_10_countries['cases'], color='blue', label='Cases')
plt.barh(top_10_countries['country'], top_10_countries['deaths'], color='red', label='Deaths')
plt.xlabel('Number of Cases and Deaths')
plt.title('Top 10 Countries with COVID-19 Cases and Deaths')
plt.legend()
plt.tight_layout()
plt.show()

# Plotting: Active Cases vs Recovered (for the top 10 countries)
plt.figure(figsize=(12, 6))
plt.barh(top_10_countries['country'], top_10_countries['active'], color='orange', label='Active Cases')
plt.barh(top_10_countries['country'], top_10_countries['recovered'], color='green', label='Recovered')
plt.xlabel('Number of Active and Recovered Cases')
plt.title('Top 10 Countries with Active and Recovered COVID-19 Cases')
plt.legend()
plt.tight_layout()
plt.show()


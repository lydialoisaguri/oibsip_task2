# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the first dataset
unemployment_data1 = pd.read_csv('/content/Unemployment in India.csv')

# Load the second dataset
unemployment_data2 = pd.read_csv('/content/Unemployment_Rate_upto_11_2020.csv')

# Explore and clean dataset 1
print("Unemployment in India")
print(unemployment_data1.head())
print('\nInfo:')
print(unemployment_data1.info())

# Handling missing value (if any)
unemployment_data1.dropna(inplace=True) # Drop rows with missing values

# Drop duplicate rows
unemployment_data1.drop_duplicates(inplace=True)

# Remove leading spaces from column name
unemployment_data1.columns = unemployment_data1.columns.str.strip()

# Plotting the histogram for dataset 1
plt.figure(figsize=(8, 6))
sns.histplot(data=unemployment_data1, x='Estimated Unemployment Rate (%)', bins=20)
plt.title('Distribution of Estimated Unemployment Rate')
plt.xlabel('Estimated Unemployment Rate (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Descriptive Analysis for dataset 1
descriptive_stats = unemployment_data1.describe()
print("Descriptive Statistics:")
print(descriptive_stats)

# Explore and clean dataset 2
print("\n Unemployment Rate upto 11 2020")
print(unemployment_data2.head())
print('\nInfo:')
print(unemployment_data2.info())

# Handling missing value (if any)
unemployment_data2.dropna(inplace=True) # Drop rows with missing values

# Drop duplicate rows
unemployment_data2.drop_duplicates(inplace=True)

# Remove leading spaces from column name
unemployment_data2.columns = unemployment_data2.columns.str.strip()

# Plotting the histogram for dataset 2
plt.figure(figsize=(8, 6))
sns.histplot(data=unemployment_data2, x='Estimated Unemployment Rate (%)', bins=20)
plt.title('Distribution of Estimated Unemployment Rate')
plt.xlabel('Estimated Unemployment Rate (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Descriptive Analysis for dataset 2
descriptive_stats = unemployment_data2.describe()
print("Descriptive Statistics:")
print(descriptive_stats)

# Combine datasets if they have similar columns
combined_unemployment_data = pd.concat([unemployment_data1, unemployment_data2], ignore_index=True)

# Display combined columns
print('Combined Columns:')
print(combined_unemployment_data.columns)

# Clean up column names
combined_unemployment_data.columns = combined_unemployment_data.columns.str.strip()

# Analyze and visualize combined data
# Plotting the unemployment rate over time for different regions
plt.figure(figsize=(10, 6))
sns.lineplot(data=combined_unemployment_data, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title('Unemployment Rate Over Time (Combined Dataset)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend(title='Region')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Descriptive Analysis
descriptive_stats = combined_unemployment_data.describe()
print("Descriptive Statistics:")
print(descriptive_stats)

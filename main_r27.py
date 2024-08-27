import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# Set the backend to Agg (non-interactive)
matplotlib.use('Agg')

# Define the file path
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0082__Day78_Linear_Regression_and_Seaborn_Data_Visualization__240826\NewProject\r00-r09 START\r00_env_START\cost_revenue_dirty.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Convert the Release_Date column to datetime format
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')

# Extract the year from the release date
df['Release_Year'] = df['Release_Date'].dt.year

# Define a function to clean the currency columns
def clean_currency(column):
    return column.replace({r'\$': '', ',': ''}, regex=True).astype(int)

# Clean the necessary columns
df['USD_Production_Budget'] = clean_currency(df['USD_Production_Budget'])
df['USD_Worldwide_Gross'] = clean_currency(df['USD_Worldwide_Gross'])

# Create a new DataFrame that excludes films not yet screened
cutoff_date = pd.to_datetime('2018-05-01')
data_clean = df.query('Release_Date <= @cutoff_date')

# Calculate the decade for each movie using floor division
data_clean['Decade'] = (data_clean['Release_Year'] // 10) * 10

# Verify the result
print(data_clean[['Release_Year', 'Decade']].head(10))

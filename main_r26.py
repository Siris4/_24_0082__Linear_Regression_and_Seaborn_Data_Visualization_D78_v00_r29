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

# Set up the plot with specific size and resolution
plt.figure(figsize=(12, 6), dpi=200)

# Create the bubble plot using Seaborn
ax = sns.scatterplot(data=data_clean,
                     x='Release_Year',
                     y='USD_Production_Budget',
                     hue='USD_Worldwide_Gross',
                     size='USD_Worldwide_Gross',
                     sizes=(20, 200),
                     palette='viridis',  # Color palette for the bubbles
                     legend='full')

# Customize the axes
ax.set(ylim=(0, 450000000),
       ylabel='Budget in $100 millions',
       xlabel='Release Year')

# Adjust the x-axis limits and ticks
ax.set_xlim(data_clean['Release_Year'].min(), data_clean['Release_Year'].max())
ax.set_xticks(range(1920, 2020, 20))  # Set x-ticks every 20 years

# Place the legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='USD_Worldwide_Gross')

# Save the plot as an image
plt.savefig('bubble_chart_with_years.png')

# Optionally, show the plot if using an interactive environment
# plt.show()

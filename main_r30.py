import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.linear_model import LinearRegression

# Initialize the LinearRegression object
regression = LinearRegression()

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

# Create two DataFrames: old films (Decade <= 1960) and new films (Decade > 1960)
old_films = data_clean[data_clean['Decade'] <= 1960]
new_films = data_clean[data_clean['Decade'] > 1960]

# Prepare data for Linear Regression
# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Fit the Linear Regression model
regression.fit(X, y)

# Output the coefficients
theta_one = regression.coef_[0][0]
theta_zero = regression.intercept_[0]
print(f"Theta-One (Slope): {theta_one}")
print(f"Theta-Zero (Intercept): {theta_zero}")

# Set up the plot with specific size and resolution
plt.figure(figsize=(8, 6), dpi=200)

# Apply the darkgrid style and create the regression plot for new films
with sns.axes_style("darkgrid"):
    sns.regplot(data=new_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'color': '#2f4b7c', 'alpha': 0.7},  # Dark blue dots
                line_kws={'color': '#ff7c43'})  # Orange line

    # Set limits on the axes so they don't show negative values
    plt.xlim(0)
    plt.ylim(0)

    # Label the axes
    plt.xlabel("Budget in $ millions")
    plt.ylabel("Revenue in $ billions")

# Save the plot as an image
plt.savefig('regplot_new_films_styled.png')

# Optionally, show the plot if u

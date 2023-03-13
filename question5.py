import pandas as pd

# Read the answer of the 4th question (imputed version of the data)

df = pd.read_csv(r'C:\Users\enesi\Desktop\P.I. Works\data_imputed.csv')

# Group the data by country and calculate the median daily vaccination numbers

grouped = df.groupby('country')['daily_vaccinations'].median().reset_index()

# Sort the countries based on their median daily vaccination numbers in descending order

sorted_countries = grouped.sort_values(by='daily_vaccinations', ascending=False)

print(sorted_countries.head(3))


import pandas as pd

# Read the answer of the 4th question (imputed version of the data)

df = pd.read_csv(r'C:\Users\enesi\Desktop\P.I. Works\data_imputed.csv')

# Create the date filter 

date_filter = df['date'] == '1/6/2021'

# Get the filtered data

filtered_data = df[date_filter]

# Calculate the total vaccinations for the given date

total_vaccinations = filtered_data['daily_vaccinations'].sum()

print(total_vaccinations)
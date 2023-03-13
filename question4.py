import pandas as pd

# Read csv file

df = pd.read_csv(r'C:\Users\enesi\Downloads\country_vaccination_stats.csv')

# Impute missing daily_vaccinations data

df['daily_vaccinations'].fillna(df.groupby('country')['daily_vaccinations'].transform('min'), inplace=True)

# Impute the countries that not have any valid vaccination number

df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)


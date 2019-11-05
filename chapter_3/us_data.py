# Following are shell commands to download the data
#curl -O https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv
#
# !curl -O https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-areas.csv
#
# !curl -O https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-abbrevs.csv
#

import pandas as pd

pop = pd.read_csv('state-population.csv')
areas = pd.read_csv('state-areas.csv')
abbrevs = pd.read_csv('state-abbrevs.csv')

print(pop.head())
print(areas.head())
print(abbrevs.head())

merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', 1)
print(merged.head())

print("null data?")
print(merged.isnull().any())

print("What is it?")
print(merged[merged['population'].isnull()].head())


print(merged.loc[merged['state'].isnull(), 'state/region'].unique())

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
print(merged.isnull().any())

final = pd.merge(merged, areas, on='state', how='left')
print(final.head())

print("Check for NULLS")
print(final.isnull().any())

print("Which ones")
print(final['state'][final['area (sq. mi)'].isnull()].unique())

final.dropna(inplace=True)
print(final.head())

data2010 = final.query("year == 2010 & ages =='total'")
print(data2010.head())

data2010.set_index('state',inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
print(density.head())
print(density.tail())
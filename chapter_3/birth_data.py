# shell command to download the data:
# !curl -O https://raw.githubusercontent.com/jakevdp/data-CDCbirths/# master/births.csv

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np

births = pd.read_csv('births.csv')
print(births.head())

births['decade'] = 10 * (births['year'] // 10)
print(births.pivot_table('births', index='decade', columns='gender', aggfunc='sum'))

sns.set()
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('totals births per year')

quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)
births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek
births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day')

print("Births By Day of the Year")
births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
print(births_by_date.head())
births_by_date.index = [pd.datetime(2012, month, day) for (month, day) in births_by_date.index]
print(births_by_date.head())
fig, ax = plt.subplots(figsize=(12,4))
print(births_by_date.plot(ax=ax))

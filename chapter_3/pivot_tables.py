import numpy as npo
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head())

print("Group By Examples")
print(titanic.groupby('sex')[['survived']].mean())
print(titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack(0))

print("Pivot Table Examples")
print(titanic.pivot_table('survived', index='sex', columns='class'))

age = pd.cut(titanic['age'], [0, 18, 80])
print(titanic.pivot_table('survived', ['sex', age], 'class'))

fare = pd.qcut(titanic['fare'], 2)
print(titanic.pivot_table('survived', ['sex', age], [fare, 'class']))

print(titanic.pivot_table(index='sex', columns='class', aggfunc={'survived':sum, 'fare':'mean'}))
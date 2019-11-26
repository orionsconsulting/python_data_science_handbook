import seaborn as sns
import numpy as np
import pandas as pd

planets = sns.load_dataset('planets')
print("planets.shape")
print(planets.shape)

print("planets.head")
print(planets.head())

rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
print(ser)

print(ser.sum())
print(ser.mean())

df = pd.DataFrame(
    {'A': rng.rand(5),
     'B': rng.rand(5)}
)

print("df")
print(df)
print("df.mean")
print(df.mean())
print(df.mean(axis='columns'))

print("describe function")
print(planets.dropna().describe())

print("groupby example")
print(planets.groupby('method')['orbital_period'].median())

for(method, group ) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))

print(planets.groupby('method')['year'].describe().unstack())

decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
print(planets.groupby(['method', decade])['number'].sum().unstack().fillna(0))
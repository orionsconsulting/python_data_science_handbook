import pandas as pd
import numpy as np

df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
                    columns=['name', 'drink'])

print(df6)
print(df7)
print(pd.merge(df6, df7))
print("inner joins")
print(pd.merge(df6, df7, how='inner'))
print("outer joins")
print(pd.merge(df6, df7, how='outer'))
print("left joins")
print(pd.merge(df6, df7, how='left'))
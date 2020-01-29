import pandas as pd

data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
names = pd.Series(data)
print(names)
print(names.str.capitalize())

import numpy as np
import pandas as pd

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data,ind)

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

print(np.concatenate([x, y, z]))

x = [[1, 2], [3, 4]]
print(np.concatenate([x, x], axis=1))


print('Simple Concatenation with pd.concat')
ser1 = pd.Series(['A', 'B', 'C'], index=[1,2,3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4,5,6])

print(pd.concat([ser1, ser2]))

df1 = make_df('AB', [1,2])
df2 = make_df('AB', [3, 4])

print(df1)
print(df2)
print(pd.concat([df1, df2]))


df3 = make_df('AB', [0,1])
df4 = make_df('CD', [0,1])
print(df3)
print(df4)
print(pd.concat([df3, df4], axis=1))

x = make_df('AB', [0,1])
y = make_df('AB', [2,3])
y.index = x.index
print("x: ")
print(x)
print("y: ")
print(y)
print("concat x and y: ")
print(pd.concat([x,y]))

print("Catch Duplicate indexes")
try:
    pd.concat([x,y], verify_integrity=True)
except ValueError as e:
    print("ValueError: ", e)

print("ignoring the index")
print(x)
print(y)
print(pd.concat([x,y], ignore_index=True))

print("Adding MultiIndex keys")
print(x)
print(y)
print(pd.concat([x,y], keys=['x','y']))

print("concatenation with joins")
df5 = make_df('ABC', [1,2])
df6 = make_df('BCD', [3,4])
print(df5)
print(df6)
print(pd.concat([df5, df6]))

print("inner joins")
print(df5)
print(df6)
print(pd.concat([df5, df6], join='inner'))

print("inner joins on columns")
print(df5)
print(df6)
print(pd.concat([df5, df6], join_axes=[df5.columns]))

print('append')
print(df1)
print(df2)
print(df1.append(df2))




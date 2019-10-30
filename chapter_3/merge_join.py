import pandas as pd
import numpy as np

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering','Engineering', 'HR']
                    }
                   )
df2 = pd.DataFrame(
    {
        'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
        'hire_date': [2004, 2008, 2012,2014]
    }
)
print(df1)
print(df2)
df3 = pd.merge(df1, df2)
print(df3)

print("Many-to-one joins")
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                           'supervisor': ['Carly', 'Guido', 'Steve']})
print(df3)
print(df4)
print(pd.merge(df3, df4))

print("Many-to-many joins")
df5 = pd.DataFrame({
    'group': ['Accounting', 'Accounting', 'Engineering', 'Engineering', 'HR', 'HR'],
    'skills': ['math', 'spreadsheets', 'coding', 'linux', 'spreadsheets', 'organization']
})
print(df1)
print(df5)
print(pd.merge(df1, df5))

print("Specification of the Merge Key")
print(df1)
print(df2)
print(pd.merge(df1, df2, on='employee'))

print("The left_on and right_on keywords")
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]
                    })

print(df1)
print(df2)
print(pd.merge(df1, df3, left_on='employee', right_on='name'))
print(pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1))

print("The left_index and right_index keywords")
df1a= df1.set_index('employee')
df2a = df2.set_index('employee')
print(df1a)
print(df2a)
print(pd.merge(df1a, df2a, left_index=True, right_index=True))

print("joins")
print(df1a)
print(df2a)
print(df1a.join(df2a))
print(pd.merge(df1a, df3, left_index=True, right_on='name'))



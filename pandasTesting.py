import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('loan-train.csv')
print(df.head())
print(df.dtypes)
print(df[ ['Credit_History', 'Education'] ])
print(df['Education'].replace({'Graduate': 1, 'Not Graduate': 0}))

def booleanToInt(val):
    try:
        if val.lower() == 'yes' or val.lower() == 'y':
            return 1
        elif val.lower() == 'no' or val.lower() == 'n':
            return 0
        else:
            return val
    except:
        return val


print(df.map(booleanToInt))
print(df['Married'].apply(booleanToInt))
df['Married'] = df['Married'].apply(booleanToInt)
print(df)


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'columna': [45,67, 989]
    })
print(df)
print(df.apply(np.mean, axis = 0))

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('loan-train.csv')
print(df['Credit_History'])
print(df.dtypes)
print(df[ ['Credit_History', 'Education'] ])
print(df['Education'].replace({'Graduate': 1, 'Not Graduate': 0}))

def booleanToInt(row):
    print('booleanToInt row: ')
    print(row)
    return 1 if row.all() else 0
    
print(df.apply(booleanToInt, axis = 1))




df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
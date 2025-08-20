import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('loan-train.csv')
print(df['Credit_History'])
print(df.dtypes)
print(df[ ['Credit_History', 'Education'] ])
print(df['Education'].replace({'Graduate': 1, 'Not Graduate': 0}))

def booleanToInt(value):
    print('booleanToInt value: ')
    print(value)
    return ''
print(df.apply(booleanToInt))




df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
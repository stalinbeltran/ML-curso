import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('loan-train.csv')
print(df['Credit_History'])
print(df.dtypes)
print(df[ ['Credit_History', 'Education'] ])
print(df['Education'].replace({'Graduate': 1, 'Not Graduate': 0}))

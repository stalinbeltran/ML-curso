import pandas as pd
import numpy as np
from scipy import stats

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'columna': [45,67, 989]
    }, index = ['primero', 'segundo', 'tercero'])
print(df)
print(df.apply(np.mean, axis = 0))
print(df.loc['segundo'])    #second row
print(df.iloc[2])       #third row


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
print(df.map(lambda x: 1 if x == 'Y' else x))
print(df.map(lambda x: 0 if x == 'N' else x))
print(df['ApplicantIncome'] > 8000)
print((df['ApplicantIncome'] > 8000)[0])
print((df['ApplicantIncome'] > 8000)[611])
print(df[df['ApplicantIncome'] > 8000])
print(df.loc[df['ApplicantIncome'] > 8000])
print(df.filter(items=['ApplicantIncome', 'Married']))
print(df.filter(like = 'Income', axis = 1))
print(df.filter(like = 'Y', axis = 0))



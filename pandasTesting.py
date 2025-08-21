import pandas as pd
import numpy as np
from scipy import stats

print('''
____________________________________________________________________________
                                **************
____________________________________________________________________________
''')


df = pd.DataFrame({
    'columna A': [1, 2, 3],
    'columna B': [4, 5, 6],
    'columna C': [45,67, 989]
    }, index = ['primero', 'segundo', 'tercero'])
    

print('\n')
print('original data frame: ')
print(df)
print('\n')
print('mean of a colum: ')
print(df.apply(np.mean, axis = 0))
print('\n')
print('mean of a row: ')
print(df.apply(np.mean, axis = 1))
print('\n')
print(df.loc['segundo'])    #second row
print('\n')
print(df.iloc[2])       #third row
print('\n')
print('std of every col: ')
print(df.apply(np.std, axis = 0))


#exit()

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
print(df[df['Loan_Status'] == 'N'])
print(df.query('(ApplicantIncome) > 9000'))
print(df.mask(df == 'Y', 1))
print(df.memory_usage())
print(df['ApplicantIncome'].max())
print(df['ApplicantIncome'][df['ApplicantIncome'] > df['ApplicantIncome'].max()*0.5])


print('\n')
print('std of every col: ')
print(df.columns[0])
print(df.drop('Loan_ID', axis = 1))
print(df[ ['Married', 'ApplicantIncome'] ].apply(np.std, axis = 0))

print('\n')
print('mean of every col: ')
print(df[ ['Married', 'ApplicantIncome'] ].apply(np.mean, axis = 0))


print('\n')
print('z-score of every value of "ApplicantIncome" column: ')
print(stats.zscore(df['ApplicantIncome']))

print('\n')
print('zscore of 2 cols: ')
print(df[ ['Married', 'ApplicantIncome'] ].apply(stats.zscore, axis = 0, nan_policy='omit'))


print('\n')
print('zscore of 2 cols + dropna: ')
print(df[ ['Married', 'ApplicantIncome'] ].apply(stats.zscore, axis = 0, nan_policy='omit').dropna())


print('\n')
print('z-score of every value of "ApplicantIncome" column + dropna: ')
print(df[ ['ApplicantIncome'] ].apply(stats.zscore, axis = 0, nan_policy='omit').dropna())

print('\n')
print('show Married and ApplicantIncome types: ')
print(df[ ['Married', 'ApplicantIncome'] ].dtypes)

print('\n')
print('show Married and ApplicantIncome: ')
print(df[ ['Married', 'ApplicantIncome'] ])

print('\n')
print('show na rows: ')
print(df[ ['Married', 'ApplicantIncome'] ][df['Married'].isna()] )


print('\n')
print('Married is na?: ')
print(df['Married'].isna())


print('\n')
print('show rows where Married nan: ')
#print( df['Married'].where(df['Married'].isna() == False) )
print( df[df['Married'].isna()] )



print('\n')
print('show rows 0, 228, 259, 500: ')
#print( df['Married'].where(df['Married'].isna() == False) )
print( df.iloc[ [0, 228, 259, 500]] )

print('\n')
print('Married is NaN?: ')
print(df['Married'].where((df['Married'] == np.nan) == True))
print( df['Married'].where(df['Married'] != np.nan) )

print('\n')
print('Married == NaN?: ')
print(df[df['Married'].isna()])



print('\n')
print('query Married == 0 : ')
print( df.query("@df['Married'] == 0") )

print('\n')
print('query Married == 3+ : ')
print( df.query("@df['Dependents'] == '3+'") )


# print('\n')
# print('query Gender == np.nan (no funciona): ')
# print( df.query("@df['Gender'] == @np.nan") )       # '>' not supported between instances of 'numpy._ArrayFunctionDispatcher' and 'int'


print('\n')
print('query Gender == Male: ')
print( df.query("@df['Gender'] == 'Male'") )





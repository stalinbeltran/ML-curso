import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import missingno as msno  # Optional: for visualizing missing data
import matplotlib.pyplot as plt


# Load your dataset into a pandas DataFrame
df = pd.read_csv('loan-train.csv')  # Replace 'your_dataset.csv' with your actual file path
# = pd.read_csv('minitest.csv')  # Replace 'your_dataset.csv' with your actual file path

# Display the first few rows of the dataset
print(df.head())

# Visualize missing data (optional)
#msno.matrix(df)
#msno.heatmap(df)
#plt.show()

# Drop rows with missing values
df_cleaned = df.dropna()
#msno.matrix(df_cleaned)
#msno.heatmap(df_cleaned)
#plt.show()

# Or, fill missing values with the mean
#df_filled = df.fillna(df.mean())


# One-hot encoding for categorical variables
df_encoded = pd.get_dummies(df_cleaned, columns=['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status'])
print(df_encoded.head())

columns = df_encoded.columns[range(1, 14)]
print(columns)

df_dropped = df_encoded.drop(df_encoded.columns[range(1)], axis= 1)
print(df_dropped.columns[7])
df_dropped = df_dropped.drop(df_dropped.columns[range(7, 19)], axis= 1)
print(df_dropped.head())
ncolums = df_dropped.shape[1]
print('ncolums. ', ncolums)
#pd.to_numeric(df['A'], errors='coerce').notnull().all())
df_numeric = df_dropped.apply(pd.to_numeric, errors='coerce')
df_numeric = df_numeric.dropna()
print(df_numeric)

#exit()


#df_encoded.plot()
#plt.show()


# Identify outliers using Z-score
from scipy import stats

applicant = df_numeric['ApplicantIncome']
z_scores = np.abs(stats.zscore(applicant))
print('z_scores: ', z_scores)


df_no_outliers = df_numeric[(z_scores < 3)]
print('df_no_outliers : ', len(df_no_outliers))
print('df_no_outliers: ', df_no_outliers)


df_outliers = df_numeric[(z_scores >= 3)]
print('df_outliers: ', df_outliers)

# Or cap outliers at a threshold
# upper_limit = df_cleaned['column_name'].quantile(0.95)
# df_cleaned['column_name'] = np.where(df_cleaned['column_name'] > upper_limit, upper_limit, df_cleaned['column_name'])


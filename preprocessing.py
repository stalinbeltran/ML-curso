import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import missingno as msno  # Optional: for visualizing missing data
import matplotlib.pyplot as plt


# Load your dataset into a pandas DataFrame
df = pd.read_csv('loan-train.csv')  # Replace 'your_dataset.csv' with your actual file path
# = pd.read_csv('minitest.csv')  # Replace 'your_dataset.csv' with your actual file path

# Display the first few rows of the dataset
#print(df.head())

# Visualize missing data (optional)
msno.matrix(df)
msno.heatmap(df)
plt.show()

# Drop rows with missing values
df_cleaned = df.dropna()
msno.matrix(df_cleaned)
msno.heatmap(df_cleaned)
plt.show()

# Or, fill missing values with the mean
#df_filled = df.fillna(df.mean())
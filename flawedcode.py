import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


def load_data(filepath):
    return pd.read_csv(filepath)

def handle_missing_values(df):
    return df.dropna()

def remove_outliers(df):
    df = df[df.columns[0:9]]
    print(df)
    z = stats.zscore(df)
    #z = stats.zscore(df['Married_No'])
    #print(z)
    exit()
    df = df.drop(df.columns[range(7, 18)], axis= 1)
    z_scores = np.abs(stats.zscore(df))
    
    return df[(z_scores < 3).all(axis=1)]

def scale_data(df):
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

def encode_categorical(df, categorical_columns):
    return pd.get_dummies(df, columns=categorical_columns)

def save_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)



# Load dataset
df = load_data('loan-train.csv')
#data preprocessing
df = encode_categorical(df, ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area'])
df = handle_missing_values(df)
ynMapping = {'Y': 1, 'N': 0}
df['Loan_Status'] = df['Loan_Status'].map(ynMapping)
print(df['Loan_Status'])

#boolean replace:
booleanMapping = {True: 1, False: 0}
df = df.replace(booleanMapping)
print(df.head())

print('data types:')
print(df.dtypes)
print(df['Loan_ID'])
df = df.drop('Loan_ID', axis= 1)
df['Dependents'] = pd.to_numeric(df['Dependents'], errors='coerce')
print(df.dtypes)
df = remove_outliers(df)
exit()

#data preprocessing
df = scale_data(df)


# Split the dataset into features and target (Flaw: No input validation)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
print(y)


# Split the data into training and testing sets (Flaw: Fixed random state)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a simple logistic regression model (Flaw: No model security checks)
model = LogisticRegression()
model.fit(X_train, y_train)
# Save the model to disk (Flaw: Unencrypted model saving)
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
# Load the model from disk for later use (Flaw: No integrity checks on the loaded model)
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(f'Model Accuracy: {result:.2f}')



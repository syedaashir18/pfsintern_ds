# -*- coding: utf-8 -*-
"""House_price_pred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ia4SmSi6ROYhynEaMLIKA3UgLMlWFUNF
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

df = pd.read_csv('Housing.csv')

print(df)

df.head()

# checking the number of rows and columns in the dataframe
df.shape

# check for missing values
df.isnull().sum

# statistical measures of the dataset
df.describe()

# Convert 'yes' and 'no' to 1 and 0 respectively in the entire DataFrame.
for column in df.columns:
    df[column] = df[column].replace({'yes': 1, 'no': 0})

# Remove non-numeric columns before calculating correlation.
df_numeric = df.select_dtypes(include=['number'])

# Calculate the correlation matrix.
correlation = df_numeric.corr()

# constructing a heatmap to understand the correlation

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

"""Splitting the data and target"""

X = df.drop(['price'], axis=1)
Y = df['price']

print(X,Y)

"""Splitting the data into training data and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

XGBoost Regressor
"""

# load the model
model = XGBRegressor()

!pip install pandas
!pip install scikit-learn

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Assuming X_train is your DataFrame
label_encoder = LabelEncoder()
X_train['furnishingstatus'] = label_encoder.fit_transform(X_train['furnishingstatus'])

# Now you can train your model
model.fit(X_train, Y_train)

"""Evaluation

Prediction on training data
"""

# accuracy for prediction on training data
training_data_prediction = model.predict(X_train)

print(training_data_prediction)

# R Squared Error
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print('R Sqaured Error:', score_1)
print('Mean Absolute Error:', score_2)

"""Visualize the actuale prices and predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Price")
plt.show()

"""Prediction on test data"""

# Convert 'furnishingstatus' to a categorical type.
X_test['furnishingstatus'] = X_test['furnishingstatus'].astype('category')

# accuracy for prediction on test data
test_data_prediction = model.predict(X_test)

# R Squared Error
score_1 = metrics.r2_score(Y_test, test_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print('R Sqaured Error:', score_1)
print('Mean Absolute Error:', score_2)


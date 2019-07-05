import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics


real_state_data = pd.read_csv('dataframe_cont2.csv')

X = real_state_data.drop('SalePrice', axis=1)
y = real_state_data['SalePrice']


mean_absolute = 0
mean_squared = 0
root_mean = 0

for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=99)

    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    mean_absolute += metrics.mean_absolute_error(y_test, y_pred)
    mean_squared += metrics.mean_squared_error(y_test, y_pred)
    root_mean += np.sqrt(metrics.mean_squared_error(y_test, y_pred))

mean_absolute = mean_absolute / 100
mean_squared = mean_squared / 100
root_mean = root_mean / 100

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

#print(df)

# Evaluation of the algorith

print('Mean Absolute Error:', mean_absolute)
print('Mean Squared Error:', mean_squared)
print('Root Mean Squared Error:', root_mean)


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz





real_state_data = pd.read_csv('dataframe_cont.csv')

index = real_state_data.index
columns = real_state_data.columns
values = real_state_data.values

# Check if there is null data
nullData = real_state_data.isnull().sum()
print(nullData)


# fill the data
# GarageYrBlt = real_state_data['GarageYrBlt']
# GarageYrBlt = GarageYrBlt.fillna(0, inplace=True)
# PoolQC = real_state_data['PoolQC']
#
# PoolQC = PoolQC.fillna(0, inplace=True)
#
# export_csv = real_state_data.to_csv(r'dataframe_cont.csv', index = None, header=True)
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz





real_state_data = pd.read_csv('dataframe_cont.csv')

index = real_state_data.index
columns = real_state_data.columns
values = real_state_data.values

################################################# - Categorical - #################################################################
# MSSubClass = real_state_data['MSSubClass']
# MSZoning = real_state_data['MSZoning']
# Street = real_state_data['Street']
# Alley = real_state_data['Alley']
# LotShape = real_state_data['LotShape']
# LandContour = real_state_data['LandContour']
# Utilities	= real_state_data['Utilities']
# LotConfig	= real_state_data['LotConfig']
# LandSlope	= real_state_data['LandSlope']
# Neighborhood	= real_state_data['Neighborhood']
# Condition1	= real_state_data['Condition1']
# Condition2	= real_state_data['Condition2']
# BldgType	= real_state_data['BldgType']
# HouseStyle	= real_state_data['HouseStyle']
# RoofStyle	= real_state_data['RoofStyle']
# RoofMatl	= real_state_data['RoofMatl']
# Exterior1st	= real_state_data['Exterior1st']
# Exterior2nd	= real_state_data['Exterior2nd']
# MasVnrType	= real_state_data['MasVnrType']
# MasVnrArea	= real_state_data['MasVnrArea']
# ExterQual	= real_state_data['ExterQual']
# ExterCond	= real_state_data['ExterCond']
# Foundation	= real_state_data['Foundation']
# BsmtQual	= real_state_data['BsmtQual']
# BsmtCond	= real_state_data['BsmtCond']
# BsmtExposure	= real_state_data['BsmtExposure']
# BsmtFinType1	= real_state_data['BsmtFinType1']
# BsmtFinSF1	= real_state_data['BsmtFinSF1']
# BsmtFinType2	= real_state_data['BsmtFinType2']
# BsmtFinSF2	= real_state_data['BsmtFinSF2']
# BsmtUnfSF	= real_state_data['BsmtUnfSF']
# Heating	= real_state_data['Heating']
# HeatingQC	= real_state_data['HeatingQC']
# Electrical	= real_state_data['Electrical']
# Functional	= real_state_data['Functional']
# Functional	= real_state_data['Functional']
# FireplaceQu	= real_state_data['FireplaceQu']
# GarageType	= real_state_data['GarageType']
# GarageYrBlt	= real_state_data['GarageYrBlt']
# GarageFinish	= real_state_data['GarageFinish']
# GarageQual	= real_state_data['GarageQual']
# GarageCond	= real_state_data['GarageCond']
# PavedDrive	= real_state_data['PavedDrive']
# PoolQC	= real_state_data['PoolQC']
# Fence	= real_state_data['Fence']
# MiscFeature	= real_state_data['MiscFeature']
# SaleType	= real_state_data['SaleType']
# SaleCondition	= real_state_data['SaleCondition']
# KitchenQual	= real_state_data['KitchenQual']
################################################# - Numeric - #################################################################
LotFrontage = real_state_data['LotFrontage']
LotArea = real_state_data['LotArea']
OverallQual	= real_state_data['OverallQual']
OverallCond	= real_state_data['OverallCond']
YearBuilt	= real_state_data['YearBuilt']
YearRemodAdd	= real_state_data['YearRemodAdd']
TotalBsmtSF	= real_state_data['TotalBsmtSF']
CentralAir	= real_state_data['CentralAir']
one1stFlrSF	= real_state_data['1stFlrSF']
two2ndFlrSF	= real_state_data['2ndFlrSF']
LowQualFinSF	= real_state_data['LowQualFinSF']
GrLivArea	= real_state_data['GrLivArea']
BsmtFullBath	= real_state_data['BsmtFullBath']
BsmtHalfBath	= real_state_data['BsmtHalfBath']
FullBath	= real_state_data['FullBath']
HalfBath	= real_state_data['HalfBath']
BedroomAbvGr	= real_state_data['BedroomAbvGr']
KitchenAbvGr	= real_state_data['KitchenAbvGr']
TotRmsAbvGrd	= real_state_data['TotRmsAbvGrd']
Fireplaces	= real_state_data['Fireplaces']
GarageCars	= real_state_data['GarageCars']
GarageArea	= real_state_data['GarageArea']
WoodDeckSF	= real_state_data['WoodDeckSF']
OpenPorchSF	= real_state_data['OpenPorchSF']
EnclosedPorch	= real_state_data['EnclosedPorch']
three3SsnPorch	= real_state_data['3SsnPorch']
ScreenPorch	= real_state_data['ScreenPorch']
PoolArea	= real_state_data['PoolArea']
MiscVal	= real_state_data['MiscVal']
MoSold	= real_state_data['MoSold']
YrSold	= real_state_data['YrSold']
SalePrice = real_state_data['SalePrice']

# Check if there is null data
nullData = real_state_data.isnull().sum()
print(nullData)


###fill the data


# nullData = dt.isnull().sum()
# rangeDataMin = dt.min()
# rangeDataMax = dt.max()
# meanData = dt.mean()
#
# dt2 = dt.fillna(meanData)
# nullData2 = dt2.isnull().sum()
# meanData2 = dt2.mean()
#
#
# print('null: ', nullData, '\n' + 'min: ', rangeDataMin, '\n' + 'max: ', rangeDataMax, '\n' + 'mean: ', meanData, '\n' + 'newNull: ', nullData2, '\n' + 'newMean: ', meanData2)
#
# LotFrontage = LotFrontage.fillna(LotFrontage.mean(), inplace=True)
# MasVnrArea = MasVnrArea.fillna(0, inplace=True)
# MasVnrType = MasVnrType.fillna('None', inplace=True)
# Electrical = Electrical.fillna('SBrkr', inplace=True)
# GarageYrBlt = GarageYrBlt.fillna(0, inplace=True)
# PoolQC = real_state_data['PoolQC']
#
# PoolQC = PoolQC.fillna(0, inplace=True)
#
# export_csv = real_state_data.to_csv(r'dataframe_cont.csv', index = None, header=True)
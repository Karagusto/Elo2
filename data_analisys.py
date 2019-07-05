#import plotly.plotly as py
#import plotly.graph_objs as go
#import plotly.tools as tools
#from plotly.tools import FigureFactory as FF
from matplotlib import pyplot as plt
from matplotlib import cm as cm

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import scipy



#real_state_data = pd.read_csv('Precos_Imoveis.csv')

real_state_data = pd.read_csv('dataframe_cat.csv')

index = real_state_data.index
columns = real_state_data.columns
values = real_state_data.values


# Street = real_state_data['Street']
# Condition1	= real_state_data['Condition1']
# Condition2	= real_state_data['Condition2']
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
# BsmtFinSF1	= real_state_data['BsmtFinSF1']
# BsmtFinType2	= real_state_data['BsmtFinType2']
# BsmtFinSF2	= real_state_data['BsmtFinSF2']
# BsmtUnfSF	= real_state_data['BsmtUnfSF']
# Heating	= real_state_data['Heating']
# HeatingQC	= real_state_data['HeatingQC']
# Electrical	= real_state_data['Electrical']
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
##################################################################################################################
MSSubClass = real_state_data['MSSubClass']
MSZoning = real_state_data['MSZoning']
Alley = real_state_data['Alley']
LotShape = real_state_data['LotShape']
LandContour = real_state_data['LandContour']
Utilities	= real_state_data['Utilities']
LotConfig	= real_state_data['LotConfig']
LandSlope	= real_state_data['LandSlope']
Neighborhood	= real_state_data['Neighborhood']
BldgType	= real_state_data['BldgType']
HouseStyle	= real_state_data['HouseStyle']
BldgType	= real_state_data['BldgType']
HouseStyle	= real_state_data['HouseStyle']
BsmtFinType1	= real_state_data['BsmtFinType1']
Functional	= real_state_data['Functional']
SaleType	= real_state_data['SaleType']
SaleCondition	= real_state_data['SaleCondition']
KitchenQual	= real_state_data['KitchenQual']
##################################################################################################################
# LotFrontage = real_state_data['LotFrontage']
# LotArea = real_state_data['LotArea']
# OverallQual	= real_state_data['OverallQual']
#
# YearBuilt	= real_state_data['YearBuilt']
# YearRemodAdd	= real_state_data['YearRemodAdd']
# TotalBsmtSF	= real_state_data['TotalBsmtSF']
# CentralAir	= real_state_data['CentralAir']
# one1stFlrSF	= real_state_data['1stFlrSF']
# two2ndFlrSF	= real_state_data['2ndFlrSF']
#
# GrLivArea	= real_state_data['GrLivArea']
# BsmtFullBath	= real_state_data['BsmtFullBath']
#
# FullBath	= real_state_data['FullBath']
# HalfBath	= real_state_data['HalfBath']
# BedroomAbvGr	= real_state_data['BedroomAbvGr']
#
# TotRmsAbvGrd	= real_state_data['TotRmsAbvGrd']
# Fireplaces	= real_state_data['Fireplaces']
# GarageCars	= real_state_data['GarageCars']
# GarageArea	= real_state_data['GarageArea']
# WoodDeckSF	= real_state_data['WoodDeckSF']
# OpenPorchSF	= real_state_data['OpenPorchSF']
#
# three3SsnPorch	= real_state_data['3SsnPorch']
# ScreenPorch	= real_state_data['ScreenPorch']
# PoolArea	= real_state_data['PoolArea']
#
# MoSold	= real_state_data['MoSold']
# SalePrice = real_state_data['SalePrice']




#OverallCond	= real_state_data['OverallCond']
#LowQualFinSF	= real_state_data['LowQualFinSF']
#BsmtHalfBath	= real_state_data['BsmtHalfBath']
#BsmtHalfBath	= real_state_data['BsmtHalfBath']
#KitchenAbvGr	= real_state_data['KitchenAbvGr']
#YrSold	= real_state_data['YrSold']
#MiscVal	= real_state_data['MiscVal']
#EnclosedPorch	= real_state_data['EnclosedPorch']


correlations = real_state_data.corr()
corr_sales = correlations['SalePrice'].sort_values(ascending=False)

print(corr_sales)

export_csv = corr_sales.to_csv(r'correlation_sales_cat.csv', index = None, header=True)



############################################################################ correlation plots ############################################################################################################


# names = ['LotFrontage'	'LotArea'	'OverallQual'	'OverallCond'	'YearBuilt'	'YearRemodAdd'	'Street'	'MasVnrArea'	'BsmtFinSF1'	'BsmtFinSF2'	'BsmtUnfSF'	'TotalBsmtSF'	'CentralAir'	'1stFlrSF'	'2ndFlrSF'	'LowQualFinSF'	'GrLivArea'	'BsmtFullBath'	'BsmtHalfBath'	'FullBath'	'HalfBath'	'BedroomAbvGr'	'KitchenAbvGr'	'TotRmsAbvGrd'	'Fireplaces'	'GarageYrBlt'	'GarageCars'	'GarageArea'	'WoodDeckSF'	'OpenPorchSF'	'EnclosedPorch'	'3SsnPorch'	'ScreenPorch'	'PoolArea'	'PoolQC'	'MiscVal'	'MoSold'	'YrSold'	'SalePrice']
#
# correlations = real_state_data.corr()
# # plot correlation matrix
# fig = plt.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(correlations, vmin=-1, vmax=1)
# fig.colorbar(cax)
# ticks = np.arange(0,9,1)
# ax.set_xticks(ticks)
# ax.set_yticks(ticks)
# ax.set_xticklabels(names)
# ax.set_yticklabels(names)
# plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# cmap = cm.get_cmap('jet', 30)
# cax = ax1.imshow(real_state_data.corr(), interpolation="nearest", cmap=cmap)
# ax1.grid(True)
# plt.title('Real estate correlation')
# labels = ['LotFrontage'	'LotArea'	'OverallQual'	'OverallCond'	'YearBuilt'	'YearRemodAdd'	'Street'	'MasVnrArea'	'BsmtFinSF1'	'BsmtFinSF2'	'BsmtUnfSF'	'TotalBsmtSF'	'CentralAir'	'1stFlrSF'	'2ndFlrSF'	'LowQualFinSF'	'GrLivArea'	'BsmtFullBath'	'BsmtHalfBath'	'FullBath'	'HalfBath'	'BedroomAbvGr'	'KitchenAbvGr'	'TotRmsAbvGrd'	'Fireplaces'	'GarageYrBlt'	'GarageCars'	'GarageArea'	'WoodDeckSF'	'OpenPorchSF'	'EnclosedPorch'	'3SsnPorch'	'ScreenPorch'	'PoolArea'	'PoolQC'	'MiscVal'	'MoSold'	'YrSold'	'SalePrice']
# ax1.set_xticklabels(labels, fontsize=6)
# ax1.set_yticklabels(labels, fontsize=6)
# # Add colorbar, make sure to specify tick locations to match desired ticklabels
# fig.colorbar(cax, ticks=[.75, .8, .85, .90, .95, 1])
# plt.show()
############################################################################ correlation plots ############################################################################################################





#import plotly.plotly as py
#import plotly.graph_objs as go
#import plotly.tools as tools
#from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy




real_state_data = pd.read_csv('dataframe.csv')

index = real_state_data.index
columns = real_state_data.columns
values = real_state_data.values
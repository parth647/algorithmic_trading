# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 00:07:50 2020

@author: parth
"""

import pandas_datareader as pdr
import datetime

####################
#API TO FETCH DATA
####################

aapl = pdr.get_data_yahoo('AAPL',
                          start = datetime.datetime(2006,10,1) ,
                          end = datetime.datetime(2020,1,1))

###################
#GETTING THE DATA TO LOCAL
####################

import pandas as pd
aapl.to_csv('data/aapl_stock.csv')

########################
#
##########################


########################
#converting daily data to monthly 
##########################

monthly_aapl = aapl.resample('M').mean()
print(monthly_aapl)

aapl['diff'] = aapl.Close - aapl.Open

########################
#VISUALIZE
##########################

import matplotlib.pyplot as plt 
aapl['Close'].plot(grid = True)
plt.show()

df = monthly_aapl
df['pct_change'] = (df.Close-df.Open)*100.00/(df.Open)*1.00

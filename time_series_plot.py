# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:53:24 2021

@author: kbsar
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import statistics as stat
import glob
import math
listofstation = ['Wolfcreek','Barnwell','BERMS_OldJackPine','BrightwaterCreek','ELA','HavikpakCreek','LakeOHara','ScottyCreek','StDenis','Trail Valley','WestNoseCreek']

#counter selects with file from file_time_series is used 
counter = 10

#calling files
file_time_series = glob.glob(r'New_TS\*.csv')
df = pd.read_csv(file_time_series[counter])

#convert ssr values to list
daymet = df['Daymet_Radiation'].tolist()
insitu = df['Insitu_Radiation'].tolist()
d1 = df['date'].tolist()

#change dates into datetime format
dates = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in d1]

#plot
fig, ax = plt.subplots()
ax.plot(dates, daymet,'o', label='Daymet Data', color='blue')
ax.plot(dates, insitu,'o', label='Insitu Data', color = 'red')
legend = ax.legend(loc='upper right', prop={'size': 30})
ax.tick_params(width=3,size = 10)
plt.xlabel('Date',fontsize = 50)
plt.ylabel(' Shortwave Radiation [W/m^2]',fontsize = 50)
plt.title(str(listofstation[counter]),fontsize = 70)
plt.xticks(fontsize = 40,rotation = 45)
plt.yticks(fontsize = 45)
plt.rcParams['figure.figsize']=(40,20)
mpl.rcParams['axes.linewidth'] = 5
plt.savefig('time_series_plots/'+str(listofstation[counter])+'.tif')
plt.show()


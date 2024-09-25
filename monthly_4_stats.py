# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:58:05 2021

@author: kbsar
"""


import pandas as pd
import glob
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
listofmonth = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
listofstation = ['Wolfcreek','Barnwell','BERMS_OldJackPine','BrightwaterCreek','ELA','HavikpakCreek','LakeOHara','ScottyCreek','StDenis','Trail Valley','WestNoseCreek']
counter = 0

#calling files
for file in glob.glob(r'New_TS\*.csv'):
    mean_d = []
    mean_i = []
    stndev_d = []
    stndev_i = []
    skew_d = []
    skew_i = []
    kurtosis_d = []
    kurtosis_i = []
    df = pd.read_csv(file)
    #change index to datetime dates
    dates = df['date'].tolist()
    datetime_object = [datetime.datetime.strptime(w,'%Y-%m-%d') for w in dates]
    df.index = datetime_object
    
    #append monthly statistics to above created lists
    fig, ax = plt.subplots(4,sharex = True)
    for c in np.arange(1,13,1):
        Month_data = df[df.index.month == c]
        mean_d.append(Month_data['Daymet_Radiation'].mean())        
        mean_i.append(Month_data['Insitu_Radiation'].mean()) 
        
        stndev_d.append((Month_data['Daymet_Radiation']).std())
        stndev_i.append((Month_data['Insitu_Radiation']).std())
        
        skew_d.append((Month_data['Daymet_Radiation']).skew())
        skew_i.append((Month_data['Insitu_Radiation']).skew())
        
        kurtosis_d.append((Month_data['Daymet_Radiation']).kurtosis())
        kurtosis_i.append((Month_data['Insitu_Radiation']).kurtosis())   
    
    
    #plot the list into subplots
    mpl.rcParams['axes.linewidth'] = 3
    plt.rcParams['figure.figsize']=(40,20)
    plt.tick_params(width=2,size = 7)
    plt.xlabel('Month',fontsize = 40)
    plt.xticks(fontsize = 40)
    ax[0].set_title(str(listofstation[counter]),fontsize = 40)    
    ax[0].scatter(listofmonth,mean_d,s = 100,label = 'daymet')
    ax[0].scatter(listofmonth,mean_i,s = 100,label = 'insitu')
    ax[0].legend(loc='best', prop={'size': 25})
    ax[1].scatter(listofmonth,stndev_d,s = 100)
    ax[1].scatter(listofmonth,stndev_i,s = 100)
    ax[2].scatter(listofmonth,skew_d,s = 100)
    ax[2].scatter(listofmonth,skew_i,s = 100)
    ax[3].scatter(listofmonth,kurtosis_d,s = 100)
    ax[3].scatter(listofmonth,kurtosis_i,s = 100)
    ax[0].set_ylabel('Mean',fontsize = 35)
    ax[1].set_ylabel('Standard Deviation',fontsize = 35)
    ax[2].set_ylabel('Skewness',fontsize = 35)
    ax[3].set_ylabel('Kurtosis',fontsize = 35)
    
    ax[0].tick_params(axis="y", labelsize=25) 
    ax[1].tick_params(axis="y", labelsize=25) 
    ax[2].tick_params(axis="y", labelsize=25) 
    ax[3].tick_params(axis="y", labelsize=25) 
   
    plt.savefig('monthly_stats/stats'+str(listofstation[counter])+'.tif') 
    plt.show()
    counter = counter + 1






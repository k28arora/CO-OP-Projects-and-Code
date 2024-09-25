# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:22:33 2021

@author: kbsar
"""

import pandas as pd
import glob
import numpy as np
import datetime
import statistics as stats
import matplotlib.pyplot as plt
import matplotlib as mpl


listofmonth = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
listofstation = ['Wolfcreek','Barnwell','BERMS_OldJackPine','BrightwaterCreek','ELA','HavikpakCreek','LakeOHara','ScottyCreek','StDenis','Trail Valley','WestNoseCreek']

counter = 0
#calling all files
for file in glob.glob(r'New_TS\*.csv'):
    listofMAE = []
    df = pd.read_csv(file)
    
    #change index to datetime dates
    dates = df['date'].tolist()
    datetime_object = [datetime.datetime.strptime(w,'%Y-%m-%d') for w in dates]
    df.index = datetime_object
    
    #append monthly mean values to listofMAE 
    for c in np.arange(1,13,1):
        Month_data = df[df.index.month == c]
        
        daymet = Month_data['Daymet_Radiation'].mean()
        insitu = Month_data['Insitu_Radiation'].mean()
        listofMAE.append(abs(daymet - insitu))
    
    #plot monthly MAE list fo each station
    plt.scatter(listofmonth,listofMAE,label = str(listofstation[counter])+' '+str (len(Month_data['Insitu_Radiation'])),s = 200)
    plt.plot(listofmonth,listofMAE,'--',linewidth= 4) 
    plt.tick_params(width=3,size = 10)
    plt.rcParams['figure.figsize']=(40,20)
    mpl.rcParams['axes.linewidth'] = 5
    plt.xlabel('Date',fontsize = 30)
    plt.xticks(fontsize = 30)
    plt.yticks(fontsize = 35)
    plt.ylabel('Mean Average Error (MAE)',fontsize = 30)
    plt.title('')
    counter = counter + 1
legend = plt.legend(loc='best', prop={'size': 25})
#plt.savefig('season/MAE_10_locations.tif')  
plt.show()   
    
        

        
        
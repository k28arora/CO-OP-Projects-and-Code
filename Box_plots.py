# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:12:30 2021

@author: kbsar
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import glob
import pymannkendall as mk


locations = ['Alpine','Barnwell','BERMS','BrightwaterCreek','ELA','HavikpakCreek','LakeOHara','ScottyCreek','StDenis','WestNoseCreek']
all_files = glob.glob(r'C:\Users\kbsar\OneDrive\Desktop\Time_Series_Data\*.csv')
file = [pd.read_csv(f) for f in all_files]


for a in np.arange(0,3,1):
    mpl.rcParams['axes.linewidth'] = 3
    dataframe = file[a]
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    df = dataframe.set_index('date')
    stats1 = df.groupby(pd.Grouper(freq='1Y')).describe()
    Daymet_stats = stats1['Daymet_Radiation']
    dates=Daymet_stats.index
    Mean = Daymet_stats['mean'].tolist()
    Max = Daymet_stats['max'].tolist()
    Dates = list(Daymet_stats.index)
    #Daymet_stats.to_csv(r'C:\Users\kbsar\OneDrive\Desktop\time_series_stats\t'+ str(counter)+'.csv', index = True)

    Mann_Kendall = mk.original_test(Mean)
    print(Mann_Kendall) 
    plt.scatter(dates,Mean, label= locations[a],s = 250)
    legend = plt.legend(loc='best', prop={'size': 30})
    plt.xlabel('Date',fontsize = 40)
    plt.xticks(Dates,fontsize = 20,rotation = 45)
    plt.ylabel('Shortwave Radiation [W/m^2]',fontsize = 40)
    plt.yticks(np.arange(0,max(Max),50))
    plt.title( 'Annual Mean Shortwave Radiation' ,fontsize=50)
    plt.tick_params(width = 3,size = 10)
   
    fig, ax = plt.subplots()
    
    for b in np.arange(0,len(Daymet_stats.index),1):
        w = (Daymet_stats.iloc[b,:])
        min_val = (w.loc['min'])
        q1_val = (w.loc['25%'])
        med_val = (w.loc['50%'])
        q3_val = (w.loc['75%'])
        max_val = (w.loc['max'])
        year = (w.name)
        year=(str(year)[:4])
        year=int(year)
        boxes = [
            {
                'label' : year,
                'whislo': min_val,    # Bottom whisker position
                'q1'    : q1_val,    # First quartile (25th percentile)
                'med'   : med_val,    # Median         (50th percentile)
                'q3'    : q3_val,    # Third quartile (75th percentile)
                'whishi': max_val,    # Top whisker position
                }
            ]
        ax.bxp(boxes, showfliers=False,positions = [b],widths = 0.5)
        ax.set_title("Shortwave Radiation ", fontsize = 50)
        ax.tick_params( labelsize=20)
        ax.set_ylabel("Shortwave Radiation",fontsize = 30)
        ax.tick_params(width=3,size = 10) 
    plt.rcParams['figure.figsize']=(30,15)
    plt.show()
    
    
    
    
    

    
    
   
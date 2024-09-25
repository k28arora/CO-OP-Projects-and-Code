# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:13:22 2021

@author: kbsar
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import glob
import pymannkendall as mk
import math

listofstation = ['Wolfcreek','Barnwell','BERMS_OldJackPine','BrightwaterCreek','ELA','HavikpakCreek','LakeOHara','ScottyCreek','StDenis','Trail Valley','WestNoseCreek']
counter = 0
# call in files
for file in glob.glob(r'New_TS\*.csv'):
    df = pd.read_csv(file)
    
    #determine of max ssr is in daymet or insitu  column
    if max(df['Daymet_Radiation']) >= max(df['Insitu_Radiation']):
           ssr = max (df['Daymet_Radiation'].tolist())
    else:
        ssr = max (df['Insitu_Radiation'].tolist())
    x = np.arange(0,ssr,1)
    
    #export daymet and insut ssr to list
    daymet = df['Daymet_Radiation'].tolist()
    insitu = df['Insitu_Radiation'].tolist()
    
    #filter out dates with nan values and append the rest to new lists
    new_d = []
    new_i = []
    for t in np.arange(0,len(daymet),1):
        if math.isnan(daymet[t]) or math.isnan(insitu[t]) == True:
            new_d = new_d
            new_i = new_i
        else:
            new_d.append(daymet[t])
            new_i.append(insitu[t])
    
    #find slope of points
    slope,intercept = np.polyfit(new_i, new_d,1)
            
    #find r squared    
    correlation_matrix = np.corrcoef(new_i, new_d)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    
    # finding mean squared error
    MSE = 0
    for k in np.arange(0,len(daymet), 1):
        if math.isnan(daymet[k]) or math.isnan(insitu[k]) == True:
            MSE += 0
        else:
            MSE += ((daymet[k] - insitu[k])**2)
    MSE = MSE / (len(daymet))
    
    #Mean Error
    ME = 0
    for a in np.arange(0,len(daymet), 1):
        if math.isnan(daymet[a]) or math.isnan(insitu[a]) == True:
            ME += 0
        else:
            ME += (daymet[a] - insitu[a])
    ME = abs(ME / len(daymet))

    #mean absolute error
    MAE = 0
    for w in np.arange(0,len(daymet), 1):
        if math.isnan(daymet[w]) or math.isnan(insitu[w]) == True:
            MAE += 0
        else:
            MAE += (abs(daymet[w] - insitu[w]))
    MAE = MAE / (len(daymet))

    #percent bias (PBIAS)
    PBIAS = 0
    for g in np.arange(0,len(daymet), 1):
        if math.isnan(daymet[g]) or math.isnan(insitu[g]) == True:
            PBIAS += 0
        else:
            PBIAS += (daymet[g] - insitu[g])
    sum = 0
    for p in np.arange(0,len(insitu), 1):
        if math.isnan(daymet[p]) or math.isnan(insitu[p]) == True:
            sum += 0
        else:
            sum += insitu[p]
    
    PBIAS = abs(100 * PBIAS / sum)
    stats_font = 50
    number_of_decimals = 2
    mpl.rcParams['axes.linewidth'] = 3
    
    #plottting
    plt.scatter(new_i,new_d,c = 'black')
    
    #code for line of best fit 
    #plt.plot(np.unique(new_i), np.poly1d(np.polyfit(new_i, new_d, 1))(np.unique(new_i)),c = 'orange',linewidth=10)
    plt.axis([0, ssr, 0, ssr])
    #plt.axis('scaled')
    plt.title(str(listofstation[counter]),fontsize = 70)
    #plt.figtext(0.75, 0.20,'slope  = '+ str(round((slope),number_of_decimals)),fontsize = stats_font)
    plt.figtext(0.75, 0.32,'RMSE = ' + str(round(((MSE)**(0.5)),number_of_decimals)),fontsize = stats_font)
    plt.figtext(0.75, 0.36,'MAE   = ' + str(round((MAE),number_of_decimals)),fontsize = stats_font)
    plt.figtext(0.75, 0.28,'PBIAS = ' + str(round((PBIAS),number_of_decimals)),fontsize = stats_font)
    plt.figtext(0.75, 0.40,'ME     = ' + str(round((ME),number_of_decimals)),fontsize = stats_font)
    plt.figtext(0.75, 0.20,'N        = ' + str(len(new_i)),fontsize = stats_font)
    plt.figtext(0.75, 0.24,'R2      = ' + str(round((r_squared),number_of_decimals)),fontsize = stats_font)
    plt.xlabel('Insitu [W/m^2]',fontsize = 50)
    plt.ylabel('Daymet [W/m^2]',fontsize = 50)
    plt.xticks(fontsize = 50)
    plt.yticks(fontsize = 50)
    
    plt.rcParams['figure.figsize']=(40,20)
    plt.plot(x,x, '--',c ='grey', linewidth = 10)
    #plt.savefig(r'New_one_to_one/'+str(listofstation[counter])+'.tif')
    counter += 1
    plt.show()
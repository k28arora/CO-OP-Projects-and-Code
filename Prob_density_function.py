# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:51:54 2021

@author: kbsar
"""

from scipy.stats import skew,kurtosis,norm
import pandas as pd
import glob
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import matplotlib as mpl

listofstation = ['Wolfcreek','Barnwell','BERMS_OldJackPine','BrightwaterCreek','ELA','HavikpakCreek','LakeOHara','ScottyCreek','StDenis','Trail Valley','WestNoseCreek']
counter = 0
#call in files
for file in glob.glob(r'New_TS\*.csv'):
    df = pd.read_csv(file)
    
    #find daymet/insitu mean and StnDev
    daymet = df['Daymet_Radiation'].tolist()
    insitu = df['Insitu_Radiation'].tolist()
    
    mean_d = df['Daymet_Radiation'].mean()
    std_d = df['Daymet_Radiation'].std()
    
    mean_i = df['Insitu_Radiation'].mean()
    std_i = df['Insitu_Radiation'].std()
    
    #plot using normal distribution function norm.pdf
    plt.scatter(daymet,norm.pdf(daymet,mean_d,std_d) ,label = 'daymet')
    plt.scatter(insitu,norm.pdf(insitu,mean_i,std_i) , label = 'insitu')
    legend = plt.legend(loc='best', prop={'size': 40})
    plt.xlabel('Shortwave Radiation (W/m^2)',fontsize = 40)
    plt.ylabel('Density',fontsize = 40)
    plt.xticks(fontsize = 40)
    plt.yticks(fontsize = 30)
    plt.rcParams['figure.figsize']=(40,20)
    mpl.rcParams['axes.linewidth'] = 3
    plt.tick_params(width=3,size = 10)
    plt.title(str(listofstation[counter]),fontsize = 40)
    #plt.savefig('season/'+str(listofstation[counter])+' PDF_plots.tif')
    plt.show()

    counter = counter + 1
    
    
    
    
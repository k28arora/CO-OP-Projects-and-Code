# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:52:44 2021

@author: kbsar
"""

import pandas as pd
import pymannkendall as pmk
import glob
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('All_NWT_locations.pdf')

# Define the directory name where Daymet data is stored



# Define alpha value used for mk test
alphaval = 0.05


# Initiate a new df to store the mk test results. At the end this df will be exported as a CSV
results_df = pd.DataFrame(columns=['Stn Name','Z', 'P', 'Slope', 'Intercept'])


# Loop through directory, and plot yearly ssr and export to pdf
for file in glob.glob(r'NWT_data\*'):

    # read in the csv file
    stn_df = pd.read_csv((file), header=6)
    
    #find yearly ssr mean
    df_mean = stn_df.groupby(stn_df['year']).agg({'srad (W/m^2)': ['mean']})
    df_mean.columns = df_mean.columns.droplevel(1)
    df_mean = df_mean.reset_index()
    filename = file.split('_')
    Stn_Name  = filename[1][5:]

    # convert the SSR column to a list
    ssr_list = df_mean['srad (W/m^2)'].to_list()
    date = df_mean['year'].to_list()
    
    #plot
    fig1 = plt.plot(date,ssr_list)
    #plt.plot(list2,list1)
    plt.xlabel('Date',fontsize = 40)
    plt.ylabel('Shortwave Radiation (W/m^2)',fontsize =40)
    plt.xticks(fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.ylim((min(ssr_list))-5,max(ssr_list) +5)
    plt.title(str(Stn_Name),fontsize = 50)
    plt.rcParams['figure.figsize']=(35,15)
    pp.savefig()
    plt.show()
    
pp.close()
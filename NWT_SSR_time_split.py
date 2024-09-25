# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:07:53 2021

@author: kbsar
"""

import pandas as pd
import pymannkendall as pmk
import glob


# Define the directory name where Daymet data is stored



# Define alpha value used for mk test
alphaval = 0.05


# Initiate a new df to store the mk test results. At the end this df will be exported as a CSV
results_df = pd.DataFrame(columns=['Stn Name','Z', 'P', 'Slope', 'Intercept'])
#results_df1 = pd.DataFrame(columns=['Stn Name','Z', 'P', 'Slope', 'Intercept'])

# Loop through directory containing Daymet files and perform mk test on each one. Append results to results_df
for file in glob.glob(r'NWT_data\*'):

    # read in the csv file
    stn_df = pd.read_csv((file), header=6)
    
    #find yearly mean
    df_mean = stn_df.groupby(stn_df['year']).agg({'srad (W/m^2)': ['mean']})
    df_mean.columns = df_mean.columns.droplevel(1)
    df_mean = df_mean.reset_index()
    dates = df_mean['year'].tolist()
    
    #seperate dataframe into 2 pieces
    df_mean_1980_to_2000 = df_mean[:21]
    df_mean_2001_to_2020 = df_mean[21:]
    filename = file.split('_')
    Stn_Name  = filename[1][5:] + ' 1980-2000'
    Stn_Name1  = filename[1][5:] + ' 2001-2020'
    
    # Make split dataframe ssr column into list
    first_half =df_mean_1980_to_2000['srad (W/m^2)'].to_list()
    second_half =df_mean_2001_to_2020['srad (W/m^2)'].to_list()
    
    #preform mann kendall teset on the lists
    trend, h, p, z, tau, s, var_s, slope, intercept = pmk.original_test(first_half, alpha=alphaval)
    trend1, h1, p1, z1, tau1, s1, var_s1, slope1, intercept1 = pmk.original_test(second_half, alpha=alphaval)
    
    #results_series = pd.Series([Stn_Name, z, p, slope, intercept],
                               #index=['Stn Name', 'Z', 'P', 'Slope', 'Intercept'])
    results_series1 = pd.Series([Stn_Name1, z1, p1, slope1, intercept1],
                               index=['Stn Name', 'Z', 'P', 'Slope', 'Intercept'])
    
    #results_df switches between 1980-2000 and 2001-2020,results_series is for 1980-2000  and results_series1 is for 2001-2020
    
    #results_df = results_df.append(results_series, ignore_index=True)
    #results_df = results_df.append(results_series1, ignore_index=True)
    
    #results_df.to_csv('Results_NWT_2001-2020.csv', index=False)
    
    
    #df_mean_1980_to_2000.to_csv(r'time_split_locations\1980_2000_'+str(Stn_Name)+'.csv', index = False)
    #df_mean_2001_to_2020.to_csv(r'time_split_locations\2001_2020_'+str(Stn_Name)+'.csv', index = False)
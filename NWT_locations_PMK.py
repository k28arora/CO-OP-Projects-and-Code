# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:57:10 2021

@author: kbsar
"""

import pandas as pd
import pymannkendall as pmk
import glob




# Define alpha value used for mk test
alphaval = 0.05


# Initiate a new df to store the mk test results. At the end this df will be exported as a CSV
results_df = pd.DataFrame(columns=['Stn Name','Z', 'P', 'Slope', 'Intercept'])


# Loop through directory containing Daymet files and perform mk test on each one. Append results to results_df
for file in glob.glob(r'NWT_data\*'):

    # read in the csv file
    stn_df = pd.read_csv((file), header=6)
    
    df_mean = stn_df.groupby(stn_df['year']).agg({'srad (W/m^2)': ['mean']})
    df_mean.columns = df_mean.columns.droplevel(1)
    df_mean = df_mean.reset_index()

    # convert the SSR column to a list
    ssr_list = df_mean['srad (W/m^2)'].to_list()
    

    # run mk test
    trend, h, p, z, tau, s, var_s, slope, intercept = pmk.original_test(ssr_list, alpha=alphaval)

    # parse filename for stn_id 
    filename = file.split('_')
    Stn_Name  = filename[1][5:]
    #stn_id = filename[0]
    #lat = filename[2]
    #lon = filename[4]

    # append mk results to results_df
    results_series = pd.Series([Stn_Name, z, p, slope, intercept],
                               index=['Stn Name', 'Z', 'P', 'Slope', 'Intercept'])
    results_df = results_df.append(results_series, ignore_index=True)


# export results_df
#results_df.to_csv('Results.csv', index=False)
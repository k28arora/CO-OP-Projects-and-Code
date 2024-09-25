# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:00:21 2021

@author: kbsar
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import statistics as stat
import glob

#calling in csv files
filenames_daymet= glob.glob(r'Daymet_1980s\*.csv')
filenames_insitu= glob.glob(r'Insitu_files\*.csv')

#reading csv 
df = [pd.read_csv(f, header = 6) for f in filenames_daymet]
df1 = [pd.read_csv(f1) for f1 in filenames_insitu]

#selecting which one to use
df = df[8]
df1= df1[8]
StnName = list(df1.StnName)
StnName= StnName[1]

# creating lists for daymet dates
list_of_year= df['year'].tolist()
list_of_yrday = df['yday'].tolist()

# creating lists for Insitu date and SSR
Insitu_Dates = df1['FullDate'].tolist()
Insitu_SSR  = df1['SSR'].tolist()


# turning dayemt dates into datetime format
Daymet_Dates=[]
for i in np.arange(0,len(list_of_yrday),1):
    Daymet_Dates.append (datetime.datetime(int(list_of_year[i]), 1, 1) + datetime.timedelta(int(list_of_yrday[i]) - 1))

#subsetting daymet to match insitu period
df.index = Daymet_Dates
df = df[Insitu_Dates[0]:Insitu_Dates[-1]]


#changing instu daets to datetime
Insitu_Dates = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in Insitu_Dates]    
my_time = datetime.datetime.min.time()
for e in np.arange(0,len(Insitu_Dates),1):
    Insitu_Dates[e] = (datetime.datetime.combine(Insitu_Dates[e], my_time))

#redefining Daymet ssr and date lists 
Date_Daymet = df.index.tolist()
SSR_Daymet = df['srad (W/m^2)'].tolist()

#redefining INsitu ssr and date lists
Date_Insitu = Insitu_Dates
SSR_Insitu = Insitu_SSR

#creating time series dataframe and filling it with the lists created above
Excel1 = pd.DataFrame({'0': pd.Series(Date_Daymet), '1': pd.Series(SSR_Daymet), '2': pd.Series(Date_Insitu),'3': pd.Series(SSR_Insitu)})

#mkaing column names
Excel1.columns = ['Date_Daymet', 'Daymet_Radiation', 'Date_Insitu', 'Insitu_Radiation']
new_df = pd.concat([Excel1[['Date_Daymet', 'Daymet_Radiation']].rename(columns={'Date_Daymet': 'date'}), Excel1[['Date_Insitu', 'Insitu_Radiation']].rename(
    columns={'Date_Insitu': 'date'})]).dropna(how='all')

#exporting to csv   
new_df = new_df.groupby('date',as_index=False ).apply(lambda x:x.ffill().bfill().drop_duplicates())
new_df.to_csv(r'New_TS\Time_Series_'+str(StnName)+'.csv', index = False)


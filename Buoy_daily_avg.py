# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:43:30 2022

@author: slsmit34
"""

'''
Calculate averages for all values where day = day
'''
#Import libraries
import pandas as pd  
#%%
#Methods
def openCsv (filename):
    df = pd.read_csv(filename + '.csv', skiprows=[1,2])
    return df

def clipDf (df):
    df['Date']=pd.to_datetime(df['Time (UTC)'])
    df_oct = df.loc[(df['Date'].dt.month== 10)]
    df_nov = df.loc[(df['Date'].dt.month== 11)]
    df = pd.concat([df_oct,df_nov])
    return df

def averageValues (df):
    df['Date'] = pd.to_datetime(df['Date'])
    a = df.resample('D', on='Date').mean()
    return a

def writeToCsv (df, filename):
    df.to_csv(filename + 'nov_oct_daily_avg.csv')
    
def filterCsv (filename):
    df = openCsv(filename)
    df = clipDf(df)
    dff = averageValues(df)
    writeToCsv(dff, filename)

#%%
if __name__ == "__main__":
    #Enter filename here:
    filename = 'SR_OCEAN_2021'
    
    filterCsv(filename)

  

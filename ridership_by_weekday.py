#@author: anantsalame


import numpy as np
import pandas
#import matplotlib.pyplot as plt
from ggplot import *
import datetime
turnstile_weather = pandas.read_csv("C:/anant/udacity/proj1/turnstile_data_master_with_weather.csv")
ridership_Date = turnstile_weather[['ENTRIESn_hourly','DATEn']]
ridership_Hour = turnstile_weather[['ENTRIESn_hourly','UNIT','Hour']]
ridership_Hour_grouped=ridership_Hour.groupby(['Hour','UNIT'])['ENTRIESn_hourly'].agg({'value':'mean'})
mask=ridership_Hour_grouped.groupby(level=0).agg('idxmax')
ridership_Hour_final=ridership_Hour_grouped.loc[mask['value']]
ridership_Date['Weekday']=ridership_Date['DATEn'].map(lambda x:datetime.datetime.strptime(x, '%m/%d/%y').strftime('%A'))
ridership_Date_groupby_Weekday = ridership_Date.groupby('Weekday').sum()
ridership_Date_groupby_Weekday = ridership_Date_groupby_Weekday.reset_index()
weekday_index = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
ridership_Date_groupby_Weekday['Index'] = ridership_Date_groupby_Weekday['Weekday'].map(weekday_index.get)
ridership_Date_groupby_Weekday.set_index('Index',inplace=True)
ridership_Date_groupby_Weekday.sort_index(inplace=True)
ridership_by_UNIT = turnstile_weather[['ENTRIESn_hourly','UNIT']]
ridership_by_UNIT_grouped = ridership_by_UNIT.groupby('UNIT',as_index=False).sum()
ridership_by_UNIT_grouped['unit_no'] = ridership_by_UNIT_grouped['UNIT'].map(lambda x:x[1:])
ridership_by_UNIT_grouped_filter = ridership_by_UNIT_grouped[ridership_by_UNIT_grouped['unit_no'].astype(int) < 50]
#ridership_by_UNIT.reset_index()
ridership_Hour_final.reset_index(inplace=True)
plot = ggplot(aes(x='Hour',y='value'),data=ridership_Hour_final)+geom_point()+xlim(0,25)+ylim(0,35000)+geom_text(data=ridership_Hour_final,mapping=aes(x='Hour',y='value',label='UNIT'),size=8, vjust=3, hjust=0.5)+scale_y_continuous(labels='comma')+ggtitle('stations with highest entries for each hour of the day')

#plot=ggplot(aes(x='Weekday',y='Total ENTRIESn_hourly'),data=ridership_Date_groupby_Weekday)+geom_histogram(stat='identity')+scale_y_continuous(labels='comma')+ggtitle('total no of Entries per hour for each day of the week')
#print(plot)


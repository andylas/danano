#@author: anantsalame


import numpy as np
import pandas
#import matplotlib.pyplot as plt
from ggplot import *
import datetime
turnstile_weather = pandas.read_csv("/Users/Anant/udacity/project1/turnstile_data_master_with_weather.csv")
ridership_Date = turnstile_weather[['ENTRIESn_hourly','DATEn']]
ridership_Date['Weekday']=ridership_Date['DATEn'].map(lambda x:datetime.datetime.strptime(x, '%m/%d/%y').strftime('%A'))
ridership_Date_groupby_Weekday = ridership_Date.groupby('Weekday').sum()
ridership_Date_groupby_Weekday = ridership_Date_groupby_Weekday.reset_index()
weekday_index = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
ridership_Date_groupby_Weekday['Index'] = ridership_Date_groupby_Weekday['Weekday'].map(weekday_index.get)
ridership_Date_groupby_Weekday.set_index('Index',inplace=True)
ridership_Date_groupby_Weekday.sort_index(inplace=True)
plot=ggplot(aes(x='Weekday',y='ENTRIESn_hourly'),data=ridership_Date_groupby_Weekday)+geom_histogram(stat='identity')+scale_y_continuous(labels='comma')+ggtitle('total no of Entries per hour for each day of the week')
print(plot)
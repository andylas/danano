#@author: anantsalame


import numpy as np
import pandas
#import matplotlib.pyplot as plt
from ggplot import *
import datetime
turnstile_weather = pandas.read_csv("C:\\anant\\udacity\\udacity\\turnstile_data_master_with_weather.csv")
ridership_Date = turnstile_weather[['ENTRIESn_hourly','DATEn']]
ridership_Date['Weekday']=ridership_Date['DATEn'].map(lambda x:datetime.datetime.strptime(x, '%m/%d/%y').strftime('%A'))
ridership_Date_groupby_Weekday = ridership_Date.groupby('Weekday').sum()
ridership_Date_groupby_Weekday = ridership_Date_groupby_Weekday.reset_index()
plot=ggplot(aes(x='Weekday',y='ENTRIESn_hourly'),data=ridership_Date_groupby_Weekday)+geom_histogram(stat='identity')
print(plot)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 21:42:56 2014

@author: anantsalame
"""

import numpy as np
import statsmodels.api as sm
import pandas
import datetime
from ggplot import *
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/anantsalame/udacity/turnstile_data_master_with_weather.csv')
Y = df['ENTRIESn_hourly']
X = df[['rain', 'precipi', 'Hour', 'meantempi']]
X = sm.add_constant(X)
model= sm.OLS(Y,X)
summary = model.fit()
#print(summary.summary())
daysofweek = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
dow=[]
for i in df['DATEn']:
    dayindex=datetime.datetime.strptime(i,'%m/%d/%y').weekday()
    dow.append(daysofweek[dayindex])
df['dayofweek'] = dow
#datetime.datetime.strptime(df['DATEn'],'%m/%d/%y').weekday())
df1 = pandas.read_csv('/Users/anantsalame/udacity/turnstile_forme.csv')
mytime=[]
for j in df1['TIMEn']:
    time1=datetime.datetime.strptime(j,'%H:%M:%S')
    #print(time1.minute)
    #break;
    time2 = time1.hour + time1.minute / 60 + time1.second / 3600
   # print(time2)
   # break
    mytime.append(time2)
df1['mytime'] = mytime



#print(ggplot.ggplot(df,ggplot.aes('dayofweek','ENTRIESn_hourly')) + ggplot.geom_histogram(color='green')+ggplot.ggtitle('ridership vs day of the week')+ ggplot.xlab('day of the week')+ggplot.ylab('riders'))
#ggp= ggplot(df1,aes('TIMEn','ENTRIESn_hourly')) + geom_point(color='green')+ggtitle('ridership vs time of the day')+ xlab('time of the day')+ylab('riders') + \
#scale_x_date(breaks=date_breaks('1 hour'),labels='%H:%M:%S')
#print(ggp)
df2=df[['UNIT','ENTRIESn_hourly']]
grp = df2.groupby('UNIT').sum()

#df3 = pandas.DataFrame(grp.axes[0])
#df3['ENTRIESn_hourly']=grp
grp1=grp.reset_index()
units_num=[]
for k in grp1['UNIT']:
    units_num.append(int(k[1:]))
print(ggplot(grp1,aes('UNIT','ENTRIESn_hourly'))+geom_bar(stat='identity',size=20)+ggtitle('ridership vs unit')+ xlab('station')+ylab('riders'))
#plt.bar(units_num,grp1['ENTRIESn_hourly'])
#plt.xticks(units_num,grp1['UNIT'])
#plt.show()
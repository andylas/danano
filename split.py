# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 22:06:47 2014

@author: anantsalame
"""
import datetime

st = "09:34:89"
sub_date_str = "11-20-07"
weather_date = datetime.datetime.strptime(sub_date_str,'%m-%d-%y').strftime('%y-%m-%d')
#==============================================================================
# year = weather_date.year
# month = weather_date.month
# day = weather_date.day
# new_date = str(year)[2:] + "-" + str(month) + '-' + str(day)
#==============================================================================
print(weather_date)
print(int(st.split(':')[0]))


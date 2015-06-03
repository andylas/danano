# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 00:20:12 2014

@author: anantsalame
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt
import scipy

turnstile_weather = pandas.read_csv("C:/anant/udacity/proj1/turnstile_data_master_with_weather.csv")
turnstile_weather_raining = turnstile_weather[turnstile_weather['rain']==1]
turnstile_weather_not_raining=turnstile_weather[turnstile_weather['rain']==0]
plt.figure()
turnstile_weather_raining['ENTRIESn_hourly'].hist()
turnstile_weather_not_raining['ENTRIESn_hourly'].hist()
z,p = scipy.stats.normaltest(turnstile_weather_raining['ENTRIESn_hourly'])
with_rain_mean = np.mean(turnstile_weather_raining['ENTRIESn_hourly'])
without_rain_mean = np.mean(turnstile_weather_not_raining['ENTRIESn_hourly'])
u,p = scipy.stats.mannwhitneyu(turnstile_weather_raining['ENTRIESn_hourly'],turnstile_weather_not_raining['ENTRIESn_hourly'])
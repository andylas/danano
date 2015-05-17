# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 19:36:59 2014

@author: anantsalame
"""

import numpy as np
import pandas
#from ggplot import *
def normalize_features(array):
   """
   Normalize the features in the data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma
def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost
def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """
    
    m = len(values)
    cost_history = []
    
       
    for i in range(num_iterations):
        predicted_value = np.dot(features,theta)
        theta = theta + (alpha/m) * np.dot((values - predicted_value),features)
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)
    return theta, pandas.Series(cost_history)
def plot_cost_history(alpha, cost_history):
   """This function is for viewing the plot of your cost history.
   You can run it by uncommenting this

       plot_cost_history(alpha, cost_history) 

   call in predictions.
   
   If you want to run this locally, you should print the return value
   from this function.
   """
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   """return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )"""
weather_df = pandas.read_csv("/Users/Anant/udacity/udacity/turnstile_data_master_with_weather.csv")
#features = weather_df[['rain', 'precipi', 'Hour', 'meantempi','fog','meandewpti','meanpressurei','meanwindspdi','mintempi','maxtempi','mindewpti','maxdewpti','minpressurei','maxpressurei']]
features = weather_df[['rain', 'Hour', 'meantempi','meanpressurei','mintempi','maxtempi','maxdewpti','minpressurei','maxpressurei']]

dummy_units = pandas.get_dummies(weather_df['UNIT'], prefix='unit')
features = features.join(dummy_units)
#print(features['unit_R001'])
values = weather_df['ENTRIESn_hourly']
m = len(values)

features, mu, sigma = normalize_features(features)
features['ones'] = np.ones(m)

features_array = np.array(features)
values_array = np.array(values)
alpha = 0.2 # please feel free to change this value
num_iterations = 150# please feel free to change this value

# Initialize theta, perform gradient descent
theta_gradient_descent = np.zeros(len(features.columns))
theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                        values_array, 
                                                        theta_gradient_descent, 
                                                        alpha, 
                                                        num_iterations)

plot = None
# -------------------------------------------------
# Uncomment the next line to see your cost history
# -------------------------------------------------
#plot = plot_cost_history(alpha, cost_history)
# 
# Please note, there is a possibility that plotting
# this in addition to your calculation will exceed 
# the 30 second limit on the compute servers.

predictions = np.dot(features_array, theta_gradient_descent)
num = (np.square(values_array - predictions)).sum()
den = (np.square(values_array - np.mean(values_array))).sum()
r_square = 1 -(num/den)


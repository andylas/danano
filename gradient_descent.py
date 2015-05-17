# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 22:51:22 2014

@author: anantsalame
"""
import numpy
import pandas
def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost
def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    cost_history = []
    num_theta = len(theta)
    num_values = len(values)    
    for i in num_iterations:
        theta = theta + (alpha/num_values) * numpy.dot((numpy.dot(features, theta) - values),features).sum()
        cost = compute_cost(features,values,theta)
    
        cost_history.append(cost)

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    return theta, pandas.Series(cost_history) # leave this line for the grader

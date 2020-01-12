#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:20:12 2019

@author: shane
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
  
def estimate_coef(x, y):
    
    #map dates to numeric values
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b):
            
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30)
    
    #map dates to numeric values
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
      
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('date')
    plt.ylabel('tests')
    
    plt.xticks(rotation=60)
          
    # function to show plot 
    plt.show() 
  
def main():
    
    # load date 
    dataset = pd.read_csv("google_data2.csv")
    x = dataset.date
    y = dataset.total
        
    # estimating coefficients 
    b = estimate_coef(x, y) 

    # plotting regression line 
    plot_regression_line(x, y, b)
    
main()
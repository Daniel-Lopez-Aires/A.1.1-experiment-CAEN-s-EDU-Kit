#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:28:13 2021

@author: dla


SCRIPT PRACTICA ALFA MASTER, PASADO DE MATLAB A PYTHON

"""

#   %reset                                      #to delete all the variables

#%%
#########################1), Data loading #####################3


with open('6_amplitude_60s_800mV_Bias_gain_gate_standar_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 6ampl file is',len(lines))
        
        ADC_channel_6ampl = []
        counts_6ampl = []
        for i in range(len(lines)):            
            ADC_channel_6ampl.append(float(lines[i].split()[0])) 
            counts_6ampl.append(float(lines[i].split()[1]))
            
#%%    0.1. Representacion
            
import matplotlib.pyplot as plt  #for simplicity, to not write matplotlib.pyplot
        #everytime we want to plot something

        

plt.bar(ADC_channel_6ampl,counts_6ampl, width = ADC_channel_6ampl[1]-ADC_channel_6ampl[0])        
plt.title("Dark counts rate vs Threshold 6 amp", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
plt.xlim(-500,5000)                       #limits of x axis (ojimetro)
#plt.ylim(0,)                            #limits of y axis
#

#%%


#############2) Calcs##########################
Amplitude = [x for x in range(10+1)] #turns of the amplitude of the Led driver

#I need to count the number of peaks. How can I do that??????????????????????

####For the moment, by counting:
    
N = 14 #peak number, counting the one in 0, and rejecting the one at 4000




#2@@@@@Gaussian fit@@@
#Source: http://emilygraceripka.com/blog/16

import math 
#from scipy.stats import norm               ##norm.fit() fit to gaussian
import scipy
import numpy as np
    #np contain linspaces as np.linspace(a,b,N)
from scipy.stats import norm  #to do gaussian fits


def gaussian(x, a, b, c):       #Definition of the function to use to fit the data
    return a * np.exp(- (x-b)**2 / (2 * c**2)) 

        #this is a gaussian function (more general than normal distribution)
        
        #if using math.exp the fit gives error: 
        #(only size-1 arrays can be converted to Python scalars)
        #with numpy.exp everything fine.       
        #
        #FRIENDSHIP ENDED WITH math.exp(), NOW numpy.exp() IS MY 
        #BEST FRIEND
        #

def gaussian_offset(x, a, b, c, offset):       #Definition of the function to use to fit the data
    return a * np.exp(- (x-b)**2 / (2 * c**2)) + offset

        #this is a gaussian function (more general than normal distribution)
        
        #if using math.exp the fit gives error: 
        #(only size-1 arrays can be converted to Python scalars)
        #with numpy.exp everything fine.       
        #
        #FRIENDSHIP ENDED WITH math.exp(), NOW numpy.exp() IS MY 
        #BEST FRIEND
        #
        #offset in case it is needed to desplace the gaussian above or below the
        #horizontal axis!!!

#So, lets now search the indexes for the fit:
    
#$$$$$$$$$$$$$$$$$$$N = 1$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#1st peak (aroudn 0)

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[122-1:130-1])  #-1 because python starts at 0
#and the indexes were found at the .txt reader, that starts in line 1      
y_data = np.array(counts_6ampl[122-1:130-1])

#mu, std = norm.fit(x_data)


gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data,)

opt_values = gaussian_fit[0]   #optimal values of the function to fit the data
cov_of_opt_val = gaussian_fit[1]            #covariances of the optimal values
    #the diagonal are the variance of the parameter to estimate.
    
a = opt_values[0]  
b = opt_values[1]
cc = opt_values[2]
        #similar values as the ones given by the fit function in Matlab :)

perr = np.sqrt(np.diag(cov_of_opt_val))        #standard deviation error (el 
                                                #error de toa la via vamos)
    #source: 
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html


sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title("Ajuste Gaussiano a pico de Am", fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis
##good enough, so moving on xD

#Storing of the relevant data, sigma and its error
sigma_stored = []
delta_sigma_stored = []

sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)









#$$$$$$$$$$$$$$$$$$$N = 2$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#here, an offset is needed (gauss does not work, and by looking a the graph)

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[158-1:168-1])   
y_data = np.array(counts_6ampl[158-1:168-1])

gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data-70)

opt_values = gaussian_fit[0]   #optimal values of the function to fit the data
cov_of_opt_val = gaussian_fit[1]            #covariances of the optimal values
    #the diagonal are the variance of the parameter to estimate.
    
a = opt_values[0]  
b = opt_values[1]
cc = opt_values[2]
#offset =  opt_values[3]
        #similar values as the ones given by the fit function in Matlab :)

perr = np.sqrt(np.diag(cov_of_opt_val))        #standard deviation error (el 
                                                #error de toa la via vamos)
    #source: 
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html


sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.plot(x_data, y_data-70, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title("Ajuste Gaussiano a pico de Am", fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis
##good enough, so moving on xD

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)



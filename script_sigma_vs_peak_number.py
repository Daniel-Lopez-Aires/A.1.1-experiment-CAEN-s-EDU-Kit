#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:28:13 2021

@author: dla


SCRIPT PRACTICA ALFA MASTER, PASADO DE MATLAB A PYTHON

"""

#reset to manually clear all the variables
#clear               #to clear the command windows
#%reset -f          #to clear all the variables without confirmation
#magic('reset -sf')

#######General packages useful##

import matplotlib.pyplot as plt  #for simplicity, to not write matplotlib.pyplot
        #everytime we want to plot something

import math 
#from scipy.stats import norm               ##norm.fit() fit to gaussian
import scipy 
import numpy as np
    #np contain linspaces as np.linspace(a,b,N)
from scipy.stats import norm  #to do gaussian fits

        
######3

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

        
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
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

#So, lets now search the indexes for the fit:
    
#$$$$$$$$$$$$$$$$$$$N = 1$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#1st peak (aroudn 0)
n = 1      #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[122-1:130-1])  #-1 because python starts at 0
#and the indexes were found at the .txt reader, that starts in line 1      
y_data = np.array(counts_6ampl[122-1:130-1])

#mu, std = norm.fit(x_data)

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)

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
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis
##good enough, so moving on xD

#Storing of the relevant data, sigma and its error
sigma_stored = []
delta_sigma_stored = []
N = []

sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)


#$$$$$$$$$$$$$$$$$$$N = 2$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[158-1:168-1])   
y_data = np.array(counts_6ampl[158-1:168-1])

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)


#$$$$$$$$$$$$$$$$$$$N = 3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[192-1:207-1])   
y_data = np.array(counts_6ampl[192-1:207-1])

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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
                                                
sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)


#$$$$$$$$$$$$$$$$$$$N = 4$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[225-1:243-1])   
y_data = np.array(counts_6ampl[225-1:243-1])  

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)


#$$$$$$$$$$$$$$$$$$$N = 5$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[263-1:282-1])   
y_data = np.array(counts_6ampl[263-1:282-1]) 

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)

#$$$$$$$$$$$$$$$$$$$N = 6$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[299-1:319-1])   
y_data = np.array(counts_6ampl[299-1:319-1]) 

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)

#$$$$$$$$$$$$$$$$$$$N = 7$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[335-1:356-1])   
y_data = np.array(counts_6ampl[335-1:356-1])   

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)


#$$$$$$$$$$$$$$$$$$$N = 8$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[371-1:388-1])   
y_data = np.array(counts_6ampl[371-1:388-1])   

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)


#$$$$$$$$$$$$$$$$$$$N = 9$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[407-1:423-1])   
y_data = np.array(counts_6ampl[407-1:423-1])   

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)



#$$$$$$$$$$$$$$$$$$$N = 10$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(ADC_channel_6ampl[444-1:458-1])   
y_data = np.array(counts_6ampl[444-1:458-1]) 

initial = [max(y_data), x_data[0], (x_data[1] - x_data[0]) * 5]
                #initial guesses for the fit. If None, this does not work, so this
                #is very important when having an offset! Thank you 
                #Lucas Hermann Negri (PeakUtils)
                
gaussian_fit = scipy.optimize.curve_fit(gaussian, x_data, y_data, initial)
                

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

sigma = cc/np.sqrt(2)                   #standard deviation of the gaussian fit
Delta_sigma = perr[2]/np.sqrt(2)        #error of the standar deviation
print('sigma: ' + str(sigma) + ' +/- ' + str(Delta_sigma) + ' MeV')

##Plot of the fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.plot(x_data, y_data, label = 'data')        #original data
plt.plot(x_data, gaussian(x_data, a, b, cc), 'ro', label = 'fit')
plt.title('Gaussian fit to the peak %i' %n, fontsize=24)          #title
plt.xlabel("E (MeV)", fontsize=12)                                    #xlabel
plt.ylabel("Cuentas", fontsize=12)                                    #ylabel
plt.tick_params(axis='both', labelsize=12)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x axis

#Storing
sigma_stored.append(sigma)
delta_sigma_stored.append(Delta_sigma)
N.append(n)

#%%

#############3) Representation of std##########################

#I have compared to amtlab, and python returns better results, with less error,
#so fuck matlab :)

#3.1.plot of std, sigma

plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma_stored, delta_sigma_stored, fmt='.-b', capsize = 5)
plt.title('Standar deviation vs peak number', fontsize=20)          #title
plt.xlabel("Peak number ", fontsize=10)                                    #xlabel
plt.ylabel(r'$\sigma$', fontsize=10)                                    #ylabel
plt.tick_params(axis='both', labelsize=10)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55) 
plt.savefig('sigma_vs_peaknumber_py.png', format='png')


#3.2.plot of variance, sigma^2

sigma2_stored = [x**2 for x in sigma_stored]                    #sigma^2
delta_sigma2_stored = np.multiply([x*math.sqrt(2) for x in sigma_stored], delta_sigma_stored)
    #this is the way to compute sigma*sqrt(2)*delta_sigma
    #[x*math.sqrt(2)*y, for x,y in zip(sigma_stored,delta_sigma_stored)] DO NOT WORK!!

plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma2_stored, delta_sigma2_stored, fmt='.-b', capsize = 5)
plt.title('Variance vs peak number', fontsize=20)          #title
plt.xlabel("Peak number ", fontsize=10)                                    #xlabel
plt.ylabel(r'$\sigma^2$', fontsize=10)                                    #ylabel
plt.tick_params(axis='both', labelsize=10)            #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55) 
plt.savefig('sigma2_vs_peaknumber_py.png', format='png')


# 3.3. Linear fit of both
#Could use my script or scipy, defining a linear function. Since I do not know how
#to compute r from scipy, and the formula used (derived from the formulas used in my
#script) will continue to use my script :))

def linear(x, m, n):       #Definition of the function to use to fit the data
    return m * x + n 

# delta(b) = 3 \sqrt(b^2/(N-2) * (1/r^2-1)) [T.E. 1] ==> got r

#linear_fit = scipy.optimize.curve_fit(linear, N, sigma_stored)
#r_fit = 1 / math.sqrt(1 + (len(N)-2) / linear_fit[0][0]**2 * 
                       (linear_fit[1][0,0] / 3)**2)

import RegresionLineal

ajuste = RegresionLineal.RegresionLineal(N, sigma_stored)
            #the results are the same as in my script, so awesome
            
ajuste2 = RegresionLineal.RegresionLineal(N, sigma2_stored)            

#linear_fit2 = scipy.optimize.curve_fit(linear, N, sigma2_stored)

#Sigma plot with fit

plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma_stored, delta_sigma_stored, fmt='.-r', capsize = 5)
plt.plot(N, [linear(a, ajuste['Slope'], ajuste['Intercept']) for a in N])      #fit
plt.title('Standard deviation vs peak number', fontsize=20)          #title
plt.xlabel("Peak number ", fontsize=10)                                    #xlabel
plt.ylabel(r'$\sigma$', fontsize=10)                                    #ylabel
plt.tick_params(axis='both', labelsize=10)            #size of tick labels  
plt.grid(True)                                              #show grid
plt.text(1,35, 'y = {0:1.3f} * x + {1:1.3f} ; r = {2:1.5f}'
         .format(ajuste['Slope'],ajuste['Intercept'],ajuste['r']))    #first 2 arguments are x,y position.
    #0:1.3f: 0 is 1st argument in format, 1.3f means float on 3 decimals
#plt.xlim(5.35,5.55) 
plt.savefig('sigma_vs_peaknumber_py.png', format='png')


#Sigma2 plot with fit
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma2_stored, delta_sigma2_stored, fmt='.-r', capsize = 5)
plt.plot(N, [linear(a, ajuste2['Slope'], ajuste2['Intercept']) for a in N])      #fit

plt.title('Variance vs peak number', fontsize=20)          #title
plt.xlabel("Peak number ", fontsize=10)                                    #xlabel
plt.ylabel(r'$\sigma^2$', fontsize=10)                                    #ylabel
plt.tick_params(axis='both', labelsize=10)            #size of tick labels  
plt.grid(True)                                              #show grid
plt.text(1,1200, 'y = {0:1.3f} * x + {1:1.3f} ; r = {2:1.5f}'
         .format(ajuste2['Slope'],ajuste2['Intercept'],ajuste2['r']))
#plt.xlim(5.35,5.55) 
plt.savefig('sigma2_vs_peaknumber_py.png', format='png')
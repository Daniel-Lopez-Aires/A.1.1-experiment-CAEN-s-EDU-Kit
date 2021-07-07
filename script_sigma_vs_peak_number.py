#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:28:13 2021

@author: dla

SCRIPT PARA EL EXPERIMENTO DE SIGMA VS PEAK NUMBER DEL A.1.1 DE CAEN

"""

#reset to manually clear all the variables
#clear               #to clear the command windows
#%reset -f          #to clear all the variables without confirmation
#magic('reset -sf')

#######General packages useful##

import matplotlib.pyplot as plt  #for simplicity, to not write matplotlib.pyplot
        #everytime we want to plot something

import scipy 
import numpy as np
    #np contain linspaces as np.linspace(a,b,N)

import sys                   #to import functions from other folders!!
sys.path.insert(0, '/home/dla/Python/Functions_homemade')   
            #path where I have the functions

import Fits
import pandas as pd

######3

#%%
#########################1), Data loading #####################3

data  =pd.read_csv('6_amplitude_60s_800mV_Bias_gain_gate_standar_histo.txt', 
                    sep = '	',names = ['ADC_ch', 'counts'])
        #due to the CAEN's s, the sepparator is strange. If you type ' ', it does
        #not work properly. But if you copy the space in the .txt and paste it here,
        #now it works. That is why below I have kept the other version to read this,
        #just in case :)
        
        
        
############Version to read it without pandas########
# with open('6_amplitude_60s_800mV_Bias_gain_gate_standar_histo.txt') as file_object:
            
#         lines = file_object.readlines()
#         print('the number of lines of the 6ampl file is',len(lines))
        
#         ADC_channel_6ampl = []
#         counts_6ampl = []
#         for i in range(len(lines)):            
#             ADC_channel_6ampl.append(float(lines[i].split()[0])) 
#             counts_6ampl.append(float(lines[i].split()[1]))
#####################


#%%    0.1. Representacion
            

        
plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.bar(data['ADC_ch'],data['counts'], width = data['ADC_ch'][1]-data['ADC_ch'][0])        
plt.title("Spectrum of the LED driver with amplitude 6", fontsize=22)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
plt.xlim(-500,5000)                       #limits of x axis (ojimetro)
#plt.ylim(0,)                            #limits of y axis
plt.savefig('histogram_amplitude_6_60s_800mV_bias_gain_gate_standard.png', format='png')
#

#%%


#############2) Calcs##########################
Amplitude = [x for x in range(10+1)] #turns of the amplitude of the Led driver

#I need to count the number of peaks. How can I do that??????????????????????

####For the moment, by counting:
    
N = 14 #peak number, counting the one in 0, and rejecting the one at 4000




#2@@@@@Gaussian fit@@@
#Source: http://emilygraceripka.com/blog/16



def gaussian(x, Heigh, Mean, Std_dev):
    return Heigh * np.exp(- (x-Mean)**2 / (2 * Std_dev**2)) 
    #

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

x_data = np.array(data['ADC_ch'][122-1:130-1])       #-1 because python starts at 0
                #and the indexes were found at the .txt reader, that starts in line 1      
y_data = np.array(data['counts'][122-1:130-1])

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error
sigma_stored = np.array([])
delta_sigma_stored = np.array([])
N = np.array([])

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)



#$$$$$$$$$$$$$$$$$$$N = 2$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][158-1:168-1])   
y_data = np.array(data['counts'][158-1:168-1])

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)


#$$$$$$$$$$$$$$$$$$$N = 3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][192-1:207-1])   
y_data = np.array(data['counts'][192-1:207-1])

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)

#Plot
plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.bar(x_data, y_data, label = 'data', width = x_data[1] - x_data[0], edgecolor="black")                         #original data
plt.plot(x_data, gaussian(x_data, fit['heigh'], fit['mean'], fit['sigma']), 'r--')           #fit
plt.title('Gaussian fit of the peak 3', fontsize=22)                      #title
plt.xlabel("ADC channels", fontsize=14)                                    #xlabel
plt.ylabel("Counts", fontsize=14)                                    #ylabel
plt.legend(['gaussian fit', 'data'], fontsize=16) 
plt.tick_params(axis='both', labelsize=14)                  #size of tick labels  
plt.grid(True)                                              #show grid
#plt.xlim(5.35,5.55)                                         #limits of x 
plt.savefig('gaussian_fit_peak_3.png', format='png')


#$$$$$$$$$$$$$$$$$$$N = 4$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][225-1:243-1])   
y_data = np.array(data['counts'][225-1:243-1])  

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)


#$$$$$$$$$$$$$$$$$$$N = 5$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][263-1:282-1])   
y_data = np.array(data['counts'][263-1:282-1]) 

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)

#$$$$$$$$$$$$$$$$$$$N = 6$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][299-1:319-1])   
y_data = np.array(data['counts'][299-1:319-1]) 

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)

#$$$$$$$$$$$$$$$$$$$N = 7$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][335-1:356-1])   
y_data = np.array(data['counts'][335-1:356-1])   

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)


#$$$$$$$$$$$$$$$$$$$N = 8$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][371-1:388-1])   
y_data = np.array(data['counts'][371-1:388-1])   


fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)


#$$$$$$$$$$$$$$$$$$$N = 9$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][407-1:423-1])   
y_data = np.array(data['counts'][407-1:423-1])   

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)



#$$$$$$$$$$$$$$$$$$$N = 10$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
n = n +1 #peak index

#Creation of the array needed to do the fit
x_data = np.array(data['ADC_ch'][444-1:458-1])   
y_data = np.array(data['counts'][444-1:458-1]) 

fit = Fits.Gaussian_fit(x_data,y_data)                      #fit


#Storing of the relevant data, sigma and its error

sigma_stored = np.append(sigma_stored, fit['sigma'])
delta_sigma_stored = np.append(delta_sigma_stored, fit['\Delta(sigma)'])
N = np.append(N, n)

#%%

#############3) Representation of std##########################

#I have compared to amtlab, and python returns better results, with less error,
#so fuck matlab :)

#3.1.plot of std, sigma

# plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
# plt.errorbar(N, sigma_stored, delta_sigma_stored, fmt='.-b', capsize = 5)
# plt.title('Standar deviation vs peak number', fontsize=22)          #title
# plt.xlabel("Peak number ", fontsize=14)                                    #xlabel
# plt.ylabel(r'$\sigma$', fontsize=14)                                    #ylabel
# plt.tick_params(axis='both', labelsize=14)            #size of tick labels  
# plt.grid(True)                                              #show grid
# #plt.xlim(5.35,5.55) 
# plt.savefig('sigma_vs_peaknumber_py.png', format='png')


#3.2.plot of variance, sigma^2

sigma2_stored = sigma_stored**2                    #sigma^2
delta_sigma2_stored = sigma_stored*np.sqrt(2) * delta_sigma_stored
    #this is the way to compute sigma*sqrt(2)*delta_sigma


# plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
# plt.errorbar(N, sigma2_stored, delta_sigma2_stored, fmt='.-b', capsize = 5)
# plt.title('Variance vs peak number', fontsize=22)          #title
# plt.xlabel("Peak number ", fontsize=14)                                    #xlabel
# plt.ylabel(r'$\sigma^2$', fontsize=14)                                    #ylabel
# plt.tick_params(axis='both', labelsize=14)            #size of tick labels  
# plt.grid(True)                                              #show grid
# #plt.xlim(5.35,5.55) 
# plt.savefig('sigma2_vs_peaknumber_py.png', format='png')


# 3.3. Linear fit of both
#Could use my script or scipy, defining a linear function. Since I do not know how
#to compute r from scipy, and the formula used (derived from the formulas used in my
#script) will continue to use my script :))

def linear(x, m, n):       #Definition of the function to use to fit the data
    return m * x + n 


ajuste = Fits.LinearRegression(N, sigma_stored)
            #the results are the same as in my script, so awesome
            
ajuste2 = Fits.LinearRegression(N, sigma2_stored)            

#Sigma plot with fit

plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma_stored, delta_sigma_stored, fmt='ro', capsize = 10)
plt.plot(N, [linear(a, ajuste['Slope'], ajuste['Intercept']) for a in N], linewidth=3)      #fit
plt.title('Standard deviation vs peak number', fontsize=22)          #title
plt.xlabel("Peak number ", fontsize=14)                                    #xlabel
plt.ylabel(r'$\sigma$', fontsize=14)                                    #ylabel
plt.tick_params(axis='both', labelsize=14)            #size of tick labels  
plt.grid(True)                                              #show grid
plt.legend(['linear fit','data',], fontsize=16, loc='upper left')             #legend
plt.text(6,15, 'y(x) = {0:1.3f}x + {1:1.3f} ; r = {2:1.3f}'
         .format(ajuste['Slope'],ajuste['Intercept'],ajuste['r']), fontsize=14)    #first 2 arguments are x,y position.
    #0:1.3f: 0 is 1st argument in format, 1.3f means float on 3 decimals
plt.xlim(0,15)
plt.savefig('sigma_vs_peaknumber_py.png', format='png')


#Sigma2 plot with fit
plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma2_stored, delta_sigma2_stored, fmt='ro', capsize = 10)
plt.plot(N, [linear(a, ajuste2['Slope'], ajuste2['Intercept']) for a in N], linewidth=3)      #fit

plt.title('Variance vs peak number', fontsize=22)          #title
plt.xlabel("Peak number ", fontsize=14)                                    #xlabel
plt.ylabel(r'$\sigma^2$', fontsize=14)                                    #ylabel
plt.tick_params(axis='both', labelsize=14)            #size of tick labels  
plt.grid(True)                                              #show grid
plt.legend(['linear fit','data',], fontsize=16, loc='upper left')             #legend
plt.text(5,100, 'y(x) = {0:1.3f}x + {1:1.3f} ; r = {2:1.2f}'
         .format(ajuste2['Slope'],ajuste2['Intercept'],ajuste2['r']), fontsize=14)
plt.xlim(0,15)
plt.savefig('sigma2_vs_peaknumber_py.png', format='png')


#Sigma2 plot with fit, CAENs style
plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma2_stored, delta_sigma2_stored, fmt='ro', capsize = 10)
plt.plot(N, [linear(a, ajuste2['Slope'], ajuste2['Intercept']) for a in N], linewidth=3)      #fit

plt.title('Variance vs peak number', fontsize=22)          #title
plt.xlabel("Peak number ", fontsize=14)                                    #xlabel
plt.ylabel(r'$\sigma^2$', fontsize=14)                                    #ylabel
plt.tick_params(axis='both', labelsize=14)            #size of tick labels  
plt.grid(True)                                              #show grid
plt.legend(['linear fit','data',], fontsize=16, loc='upper left')             #legend
plt.text(5,200, 'y(x) = {0:1.3f}x + {1:1.3f} ; r = {2:1.2f}'
         .format(ajuste2['Slope'],ajuste2['Intercept'],ajuste2['r']), fontsize=14) #10 default size)
plt.ylim(0,7000) 
plt.xlim(0,15)
plt.savefig('sigma2_vs_peaknumber_CAENs_style_py.png', format='png')




#%% 

########################4)Square fit to variance##########################

#the fashion to do the fit is the usual, define the funciton, and then fit:
    

#Creation of the array needed to do the fit
x_data = np.array(N)   
y_data = np.array(sigma2_stored) 

quad_fit = Fits.QuadraticRegression(x_data, y_data)

def cuadratic(x, a, b, c):       #Definition of the function to use to fit the data
    return a * x**2 + b*x + c 


#plot
plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.errorbar(N, sigma2_stored, delta_sigma2_stored, fmt='ro', capsize = 10)
plt.plot(N, [cuadratic(x, quad_fit['a'], quad_fit['b'], quad_fit['c']) for x in N], linewidth=3)      #fit

plt.title('Variance vs peak number', fontsize=22)          #title
plt.xlabel("Peak number ", fontsize=14)                                    #xlabel
plt.ylabel(r'$\sigma^2$', fontsize=14)                                    #ylabel
plt.tick_params(axis='both', labelsize=14)            #size of tick labels  
plt.grid(True)                                              #show grid
plt.legend(['quadratic fit','data',], fontsize=16, loc='upper left')             #legend
plt.text(2.7,300, 'y(x) = {0:1.3f}x^2 + {1:1.3f}x + {2:1.3f} ; r = {3:1.3f}'
         .format(quad_fit['a'], quad_fit['b'], quad_fit['c'], quad_fit['r']), fontsize=14) #10 default size
plt.xlim(0,15)
plt.savefig('sigma2_vs_peaknumber_cuadratic_fit_py.png', format='png')


#dude, that fit is sick, which would also confirm that CAEN is wrong.
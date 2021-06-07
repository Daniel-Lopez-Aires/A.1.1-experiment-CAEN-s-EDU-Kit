#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:28:13 2021

@author: dla


SCRIPT PRACTICA ALFA MASTER, PASADO DE MATLAB A PYTHON

"""
import sys                   #to import functions from other folders!!
sys.path.insert(0, '/home/dla/Python/Functions_homemade')   #path where I have the functions

import numpy as np
import Read_hist_txt
import Gaussian_fit

#   %reset                                      #to delete all the variables

#%%
#########################1), Data loading #####################3
#The files to load are in txt. The best way to read is:


#Firstly create the data by setting the led driver amplitude to 0, obtaining 
#extrange results, so will now unplug it, and closing the SiPM to see if now 
#the results are fine.



with open('0_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:            
        
    lines = file_object.readlines()
    print('the number of lines of the 0mV file is',len(lines))
        
    ADC_channel_0mV = []
    counts_0mV = []
    for i in range(len(lines)):            
        ADC_channel_0mV.append(float(lines[i].split()[0])) 
        counts_0mV.append(float(lines[i].split()[1]))
            
        
with open('10_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:        
    
    lines = file_object.readlines()
    print('the number of lines of the 100mV file is',len(lines))
        
    ADC_channel_10mV = []
    counts_10mV = []
    for i in range(len(lines)):            
        ADC_channel_10mV.append(float(lines[i].split()[0])) 
        counts_10mV.append(float(lines[i].split()[1]))


with open('20_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:                      
                 
        lines = file_object.readlines()
        print('the number of lines of the 20mV file is',len(lines))
        #This contains strings (have to be converted to numbers using int()
        #and \n, so the \n (salto de linea) have to be removed
        
        ADC_channel_20mV = []
        counts_20mV = []
        for i in range(len(lines)):            
            ADC_channel_20mV.append(float(lines[i].split()[0]))  #store 1st number of the
                            #column
            counts_20mV.append(float(lines[i].split()[1]))     #store 2nd number of the
                            #column          

with open('30_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:                     
                 
        lines = file_object.readlines()
        print('the number of lines of the 30mV file is',len(lines))
        
        ADC_channel_30mV = []
        counts_30mV = []
        for i in range(len(lines)):            
            ADC_channel_30mV.append(float(lines[i].split()[0])) 
            counts_30mV.append(float(lines[i].split()[1]))
            
with open('40_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:                       
                 
        lines = file_object.readlines()
        print('the number of lines of the 40mV file is',len(lines))
        
        ADC_channel_40mV = []
        counts_40mV = []
        for i in range(len(lines)):            
            ADC_channel_40mV.append(float(lines[i].split()[0])) 
            counts_40mV.append(float(lines[i].split()[1]))

with open('50_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:                     
                 
        lines = file_object.readlines()
        print('the number of lines of the 50mV file is',len(lines))
        
        ADC_channel_50mV = []
        counts_50mV = []
        for i in range(len(lines)):            
            ADC_channel_50mV.append(float(lines[i].split()[0])) 
            counts_50mV.append(float(lines[i].split()[1]))

with open('60_mV_55V_32dB_200_72ns_Led_0_histo.txt') as file_object:                     
                 
        lines = file_object.readlines()
        print('the number of lines of the 60mV file is',len(lines))
        
        ADC_channel_60mV = []
        counts_60mV = []
        for i in range(len(lines)):            
            ADC_channel_60mV.append(float(lines[i].split()[0])) 
            counts_60mV.append(float(lines[i].split()[1]))

            
#%%


#############2) Calcs##########################
total_counts = [sum(counts_0mV), sum(counts_10mV), sum(counts_20mV), 
                sum(counts_30mV), sum(counts_40mV), sum(counts_50mV),
                sum(counts_60mV)]
total_count_rate = [value /30 for value in total_counts]


thresholds = [0, 10, 20, 30, 40, 50, 60]

#%%

#########3) Representacion######3

    #i) Plot normal
import matplotlib.pyplot as plt  #for simplicity, to not write matplotlib.pyplot
        #everytime we want to plot something
        
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(thresholds,total_count_rate, width = thresholds[1]-thresholds[0], edgecolor="black")

# Set chart title and label axes.
plt.title("Dark counts rate vs Threshold, LED driver = 0", fontsize=22)   #title
plt.xlabel("Threshold (mV)", fontsize=14)                        #xlabel
plt.ylabel("Count rate (Hz)", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True)                                              #show grid
#plt.yscale('log')                                          #y axis in log scale
plt.savefig('Dark_counts_vs_threshold_SiPM_no_led_CAEN_oriented.png', format='png')



#%%

#Se obtiene algo rarísimo :(
#Tal vez sea pq el Led driver, aún a 0 de amplitud, envía algo? Probemos quitandolo,
#simplemente poniendole la tapa al SIPM.

#Nuevo patron haciendo eso, pero raro, es casi uniforme, salvo el del 200mV.Lo remido,
#y ahora sale muy uniforme, asi q what the fuck? no hace nada el threshold??
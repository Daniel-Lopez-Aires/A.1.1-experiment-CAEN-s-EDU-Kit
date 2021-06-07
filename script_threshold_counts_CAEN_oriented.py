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

#   %reset                                      #to delete all the variables

#%%
#########################1), Data loading #####################3
#The files to load are in txt. The best way to read is:


#Firstly create the data by setting the led driver amplitude to 0, obtaining 
#extrange results, so will now unplug it, and closing the SiPM to see if now 
#the results are fine.

counts_stored = np.array([])                          #storing variable of the counts
rate_stored = np.array([])                          #storing variable of the count rate
ADC_channel = np.array([])                          #to store the channels

time = np.array([30,30,30,30,30,30,30])              #[s] duration time od the measurements
                #600, 200, 200


####0 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('0_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values
ADC_channel = np.append(ADC_channel,load[0])
counts_stored = np.append(counts_stored,load[1])
rate_stored = np.append(rate_stored,load[2])
   
####10 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('10_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values (the 2nd storing and more has to be columns stack!!)
ADC_channel = np.column_stack((ADC_channel,load[0]))
counts_stored = np.column_stack((counts_stored,load[1]))
rate_stored = np.column_stack((rate_stored,load[2]))    
        
####20 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('20_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values (the 2nd storing and more has to be columns stack!!)
ADC_channel = np.column_stack((ADC_channel,load[0]))
counts_stored = np.column_stack((counts_stored,load[1]))
rate_stored = np.column_stack((rate_stored,load[2]))   


####30 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('30_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values (the 2nd storing and more has to be columns stack!!)
ADC_channel = np.column_stack((ADC_channel,load[0]))
counts_stored = np.column_stack((counts_stored,load[1]))
rate_stored = np.column_stack((rate_stored,load[2]))       


####40 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('40_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values (the 2nd storing and more has to be columns stack!!)
ADC_channel = np.column_stack((ADC_channel,load[0]))
counts_stored = np.column_stack((counts_stored,load[1]))
rate_stored = np.column_stack((rate_stored,load[2]))      


####50 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('50_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values (the 2nd storing and more has to be columns stack!!)
ADC_channel = np.column_stack((ADC_channel,load[0]))
counts_stored = np.column_stack((counts_stored,load[1]))
rate_stored = np.column_stack((rate_stored,load[2]))     
     
       
####60 mV##
load = Read_hist_txt.Read_hist_txt_CAEN('60_mV_55V_32dB_200_72ns_Led_0_histo.txt', time[0])  
                               
#Storing of the values (the 2nd storing and more has to be columns stack!!)
ADC_channel = np.column_stack((ADC_channel,load[0]))
counts_stored = np.column_stack((counts_stored,load[1]))
rate_stored = np.column_stack((rate_stored,load[2]))   

            
#%%


#############2) Calcs##########################
total_counts = np.array( [sum(counts_stored[:,0]), sum(counts_stored[:,1]), sum(counts_stored[:,2]), 
                sum(counts_stored[:,3]), sum(counts_stored[:,4]), sum(counts_stored[:,5]),
                sum(counts_stored[:,6])] )
total_count_rate = total_counts / time

thresholds = np.array( [0, 10, 20, 30, 40, 50, 60] )        #thresholds values

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
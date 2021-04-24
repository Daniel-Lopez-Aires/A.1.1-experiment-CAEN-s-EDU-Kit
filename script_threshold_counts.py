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
#The files to load are in txt. The best way to read is:

#0mV to be measued again!                           DONE!!!!!
#100mV too                                          DONE!!!!

#Firstly create the data by setting the led driver amplitude to 0, obtaining 
#extrange results, so will now unplug it, and closing the SiPM to see if now 
#the results are fine.

#with open('0mV_histo.txt') as file_object:
with open('0mV_tapa_histo.txt') as file_object:            
        
    lines = file_object.readlines()
    print('the number of lines of the 0mV file is',len(lines))
        
    ADC_channel_0mV = []
    counts_0mV = []
    for i in range(len(lines)):            
        ADC_channel_0mV.append(float(lines[i].split()[0])) 
        counts_0mV.append(float(lines[i].split()[1]))
            
        
#with open('100mV_histo.txt') as file_object:
with open('100mV_tapa_histo.txt') as file_object:     
    
    lines = file_object.readlines()
    print('the number of lines of the 100mV file is',len(lines))
        
    ADC_channel_100mV = []
    counts_100mV = []
    for i in range(len(lines)):            
        ADC_channel_100mV.append(float(lines[i].split()[0])) 
        counts_100mV.append(float(lines[i].split()[1]))

#with open('200mV_histo.txt') as file_object:    #file_object stores
            # the object representing the file (pi.txt), which is opened with
            #the open function
with open('200mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 200mV file is',len(lines))
        #This contains strings (have to be converted to numbers using int()
        #and \n, so the \n (salto de linea) have to be removed
        
        ADC_channel_200mV = []
        counts_200mV = []
        for i in range(len(lines)):            
            ADC_channel_200mV.append(float(lines[i].split()[0]))  #store 1st number of the
                            #column
            counts_200mV.append(float(lines[i].split()[1]))     #store 2nd number of the
                            #column          
#with open('300mV_histo.txt') as file_object:
with open('300mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 300mV file is',len(lines))
        
        ADC_channel_300mV = []
        counts_300mV = []
        for i in range(len(lines)):            
            ADC_channel_300mV.append(float(lines[i].split()[0])) 
            counts_300mV.append(float(lines[i].split()[1]))
            
#with open('400mV_histo.txt') as file_object:
with open('400mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 400mV file is',len(lines))
        
        ADC_channel_400mV = []
        counts_400mV = []
        for i in range(len(lines)):            
            ADC_channel_400mV.append(float(lines[i].split()[0])) 
            counts_400mV.append(float(lines[i].split()[1]))

#with open('500mV_histo.txt') as file_object:
with open('500mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 500mV file is',len(lines))
        
        ADC_channel_500mV = []
        counts_500mV = []
        for i in range(len(lines)):            
            ADC_channel_500mV.append(float(lines[i].split()[0])) 
            counts_500mV.append(float(lines[i].split()[1]))

#with open('600mV_histo.txt') as file_object:
with open('600mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 600mV file is',len(lines))
        
        ADC_channel_600mV = []
        counts_600mV = []
        for i in range(len(lines)):            
            ADC_channel_600mV.append(float(lines[i].split()[0])) 
            counts_600mV.append(float(lines[i].split()[1]))

#with open('700mV_histo.txt') as file_object:
with open('700mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 700mV file is',len(lines))
        
        ADC_channel_700mV = []
        counts_700mV = []
        for i in range(len(lines)):            
            ADC_channel_700mV.append(float(lines[i].split()[0])) 
            counts_700mV.append(float(lines[i].split()[1]))

#with open('800mV_histo.txt') as file_object:
with open('800mV_tapa_histo.txt') as file_object:                    
                 
        lines = file_object.readlines()
        print('the number of lines of the 800mV file is',len(lines))
        
        ADC_channel_800mV = []
        counts_800mV = []
        for i in range(len(lines)):            
            ADC_channel_800mV.append(float(lines[i].split()[0])) 
            counts_800mV.append(float(lines[i].split()[1]))
#%%


#############2) Calcs##########################
total_counts = [sum(counts_0mV), sum(counts_100mV), sum(counts_200mV), 
                sum(counts_300mV), sum(counts_400mV), sum(counts_500mV),
                sum(counts_600mV), sum(counts_700mV), sum(counts_800mV)]
total_count_rate = [value /30 for value in total_counts]
thresholds = [0, 100, 200, 300, 400, 500, 600, 700, 800]

#%%

#########3) Representacion######3

    #i) Plot normal
import matplotlib.pyplot as plt  #for simplicity, to not write matplotlib.pyplot
        #everytime we want to plot something
        
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(thresholds,total_count_rate, width = 10.0)

# Set chart title and label axes.
plt.title("Dark counts rate vs Threshold, no Led driver", fontsize=20)   #title
plt.xlabel("Threshold (mV)", fontsize=10)                        #xlabel
plt.ylabel("Count rate (Hz)", fontsize=10)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=10)              #size of axis
plt.grid(True)                                              #show grid
#plt.yscale('log')                                          #y axis in log scale
plt.savefig('Dark_counts_vs_threshold_SiPM_no_led.png', format='png')


#%%

#Se obtiene algo rarísimo :(
#Tal vez sea pq el Led driver, aún a 0 de amplitud, envía algo? Probemos quitandolo,
#simplemente poniendole la tapa al SIPM.

#Nuevo patron haciendo eso, pero raro, es casi uniforme, salvo el del 200mV.Lo remido,
#y ahora sale muy uniforme, asi q what the fuck? no hace nada el threshold??
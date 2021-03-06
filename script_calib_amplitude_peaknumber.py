#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:28:13 2021

@author: dla

NEW VERION, WITH THE NEW DATA, FROM 26_4_21
"""

#reset to manually clear all the variables
#clear               #to clear the command windows
#%reset -f          #to clear all the variables without confirmation
#magic('reset -sf')


#######General packages useful##

import matplotlib.pyplot as plt  #for simplicity, to not write matplotlib.pyplot
        #everytime we want to plot something
        
######3

plt.close("all")

#%%
#########################1), Data loading #####################3
#The files to load are in txt. The best way to read is:

#0mV to be measued again!                           DONE!!!!!
#100mV too                                          DONE!!!!

#Firstly create the data by setting the led driver amplitude to 0, obtaining 
#extrange results, so will now unplug it, and closing the SiPM to see if now 
#the results are fine.

total_counts = []       #variable that will contain the total counts of all the
                        #spectras
with open('0_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 0 amp file is',len(lines))
        
        ADC_channel_0ampl = []
        counts_0ampl = []
        for i in range(len(lines)):            
            ADC_channel_0ampl.append(float(lines[i].split()[0])) 
            counts_0ampl.append(float(lines[i].split()[1]))
       
        total_counts.append(sum(counts_0ampl))  #total counts of the spectra     
        
with open('1_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 1ampl file is',len(lines))
        
        ADC_channel_1ampl = []
        counts_1ampl = []
        for i in range(len(lines)):            
            ADC_channel_1ampl.append(float(lines[i].split()[0])) 
            counts_1ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_1ampl))  #total counts of the spectra  
        
with open('2_ampl_new_histo.txt') as file_object:    #file_object stores
            # the object representing the file (pi.txt), which is opened with
            #the open function
            
        lines = file_object.readlines()
        print('the number of lines of the 2ampl file is',len(lines))
        #This contains strings (have to be converted to numbers using int()
        #and \n, so the \n (salto de linea) have to be removed
        
        ADC_channel_2ampl = []
        counts_2ampl = []
        for i in range(len(lines)):            
            ADC_channel_2ampl.append(float(lines[i].split()[0]))  #store 1st number of the
                            #column
            counts_2ampl.append(float(lines[i].split()[1])) #store 2nd number of the
                            #column
        
        total_counts.append(sum(counts_2ampl))  #total counts of the spectra  
                         
with open('3_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 3ampl file is',len(lines))
        
        ADC_channel_3ampl = []
        counts_3ampl = []
        for i in range(len(lines)):            
            ADC_channel_3ampl.append(float(lines[i].split()[0])) 
            counts_3ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_3ampl))  #total counts of the spectra  
                       
with open('4_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 400mV file is',len(lines))
        
        ADC_channel_4ampl = []
        counts_4ampl = []
        for i in range(len(lines)):            
            ADC_channel_4ampl.append(float(lines[i].split()[0])) 
            counts_4ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_4ampl))  #total counts of the spectra  
        
with open('5_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 5ampl file is',len(lines))
        
        ADC_channel_5ampl = []
        counts_5ampl = []
        for i in range(len(lines)):            
            ADC_channel_5ampl.append(float(lines[i].split()[0])) 
            counts_5ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_5ampl))  #total counts of the spectra  
        
with open('6_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 6ampl file is',len(lines))
        
        ADC_channel_6ampl = []
        counts_6ampl = []
        for i in range(len(lines)):            
            ADC_channel_6ampl.append(float(lines[i].split()[0])) 
            counts_6ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_6ampl))  #total counts of the spectra  
        
        #some lines in the .txt deleted because it had more than 3k lines, at the
        #end several lines were repeated, so were erased
        
with open('7_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 7ampl file is',len(lines))
        
        ADC_channel_7ampl = []
        counts_7ampl = []
        for i in range(len(lines)):            
            ADC_channel_7ampl.append(float(lines[i].split()[0])) 
            counts_7ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_7ampl))  #total counts of the spectra  
        
with open('8_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 8ampl file is',len(lines))
        
        ADC_channel_8ampl = []
        counts_8ampl = []
        for i in range(len(lines)):            
            ADC_channel_8ampl.append(float(lines[i].split()[0])) 
            counts_8ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_8ampl))  #total counts of the spectra

#Files with 9 and 10 deleted because they excess the range of the spectra!!!
        
with open('9_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 9ampl file is',len(lines))
        
        ADC_channel_9ampl = []
        counts_9ampl = []
        for i in range(len(lines)):            
            ADC_channel_9ampl.append(float(lines[i].split()[0])) 
            counts_9ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_9ampl))  #total counts of the spectra  
        
with open('10_ampl_new_histo.txt') as file_object:
            
        lines = file_object.readlines()
        print('the number of lines of the 10ampl file is',len(lines))
        
        ADC_channel_10ampl = []
        counts_10ampl = []
        for i in range(len(lines)):            
            ADC_channel_10ampl.append(float(lines[i].split()[0])) 
            counts_10ampl.append(float(lines[i].split()[1]))
        
        total_counts.append(sum(counts_10ampl))  #total counts of the spectra  
        
#%%    0.1. Representacion
            


plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default      
plt.bar(ADC_channel_0ampl,counts_0ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])     
        #widht so that each bar touches each other!
plt.title("Histogram with amplitude 0 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis
plt.savefig('Spectra_LedDriver_0_ampl.png', format='png')


#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_1ampl,counts_1ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])     
plt.title("Histogram with amplitude 1 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis

#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_2ampl,counts_2ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Histogram with amplitude 2 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis

#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_3ampl,counts_3ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])          
plt.title("Histogram with amplitude 3 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis

#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_4ampl,counts_4ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])         
plt.title("Histogram with amplitude 4 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis

#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_5ampl,counts_5ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])     
plt.title("Histogram with amplitude 5 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis


#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_6ampl,counts_6ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Histogram with amplitude 6 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis
#plt.savefig('Spectra_LedDriver_0_ampl.png', format='png')

#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_7ampl,counts_7ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Histogram with amplitude 7 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis

#
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(ADC_channel_8ampl,counts_8ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Histogram with amplitude 8 of the LED driver", fontsize=24)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis

#%%


#############2) Calcs##########################
Amplitude =  [x for x in range(10+1)] 
Amplitude_min =  [x for x in range(7+1)] #since I only use from 0 to 7

#I need to count the number of peaks. How can I do that??????????????????????

#for the moment, will do it by hand:
    
number_peaks = [2, 2, 2, 3, 4, 7, 14, 25] #from the screenshots, counts from 0 to 10 turns
                #0,1,2,3,4,5,6,7(dudoso, podria contar 2 mas),              #wheel turns
#el 8 ya es un continuo practicamente
#el 9 es raro, pq est?? pegado al maximo
#el 10 no se ve, pasar?? del maximo de carga

#[3, 3, 3, 4, 5, 8, 16, 25] #values of the old version, to compare

#%%


#############3) Plot################3

plt.figure(figsize=(10,6))  #width, heigh 6.4*4.8 inches by default
plt.bar(Amplitude_min, number_peaks, width = Amplitude[1]-Amplitude[0], edgecolor="black")
        #edgecolor is the color of the borders of the bars.        
plt.title("Peak number vs Amplitude of the LED driver", fontsize=22)           #title
plt.xlabel("Amplitude of the LED driver", fontsize=14)                        #xlabel
plt.ylabel("Peak number", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis
plt.savefig('Number_of_peaks_vs_LedDriver_amplitude.png', format='png')
#%%
#############4) Discuss################3

#number of peaks increase exponentially with the amplitude. Fro the initial values, no change, but
#for 3 above it begins to increase exponentially, until 7. For 7, more peaks are seen in the left
#side of the centre of the gaussian-like structure. Why can be this? This could be due to the fact that
#needs to be proved that sigma increased with the peaknumber, so if the peaks are more broad, less peaks
#appears.
#For 8, a continuos is seen, so peak counting s no possible. 
#For 9, something appears that seems like the left side of the gaussian placed at the right, close to
#the highest values of the charge. This suggest that now the discharge has very high charge, so that
#the signal is not processed correctly.
#For 10, the last value, no signal is seen, confirming this hypothesis 
#(peak structure is moving to the right) 

#TO DISCUSS WITH MARCOS AND JUANPA

#%% ########### 5) Plot intensity-Amplitude ############

#Marcos also want this, so lets do it!


plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(Amplitude, total_counts, width = Amplitude[1]-Amplitude[0], edgecolor="black")
        #edgecolor is the color of the borders of the bars.        
plt.title("Total counts vs Amplitude of the LED driver", fontsize=20)           #title
plt.xlabel("Amplitude of the LED driver", fontsize=10)                        #xlabel
plt.ylabel("Counts", fontsize=10)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=10)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis
plt.savefig('Tota_counts_vs_LedDriver_amplitude.png', format='png')


#The numbers of total counts read in the software is (by the screeenshots)

total_counts_software = [283948, 283668, 307468, 274148, 298508, 309428, 
                         318108, 200788, 199108, 199668, 283388]  #from the software
                        #0,1,2,3,4,5,
                        #6, 7,8,9,10
                        
#total_counts_software = [217224, 235704, 239650, 215628, 199892, 191212, 288652,
#                        172452, 91252, 341012 , 308868]  #from the software
#from the old version!!
                
                #slightly different from the one computed w\ python, differences
                #around 7 counts, very little!!
                
plt.figure(figsize=(8,5))  #width, heigh 6.4*4.8 inches by default
plt.bar(Amplitude, total_counts_software, width = Amplitude[1]-Amplitude[0], edgecolor="black")
        #edgecolor is the color of the borders of the bars.        
plt.title("Total counts (SiPM_kit) vs Amplitude of the LED driver", fontsize=20)           #title
plt.xlabel("Amplitude (wheel) of the LED driver", fontsize=10)                        #xlabel
plt.ylabel("Counts", fontsize=10)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=10)              #size of axis
plt.grid(True) 
#plt.xlim(0,800)                       #limits of x axis
#plt.ylim(0,11000)                            #limits of y axis
plt.savefig('Tota_counts_software_vs_LedDriver_amplitude.png', format='png')    




#%% Plot to see the mshift of the spectra to the right

plt.figure(figsize=(13,12))  #width, heigh 6.4*4.8 inches by default
plt.suptitle("Spectra of the LED driver varying its amplitude", fontsize=22, wrap=True)           #title

plt.subplot(2, 2, 1)
plt.bar(ADC_channel_5ampl,counts_5ampl, width = ADC_channel_5ampl[1]-ADC_channel_5ampl[0])        
plt.title("Amplitude = 5", fontsize=18)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
plt.xlim(min(ADC_channel_8ampl),3000)                       #limits of x axis

plt.subplot(2, 2, 2)
plt.bar(ADC_channel_6ampl,counts_6ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Amplitude = 6", fontsize=18)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True)  
plt.xlim(min(ADC_channel_8ampl),5000)                       #limits of x axis

plt.subplot(2, 2, 3)
plt.bar(ADC_channel_7ampl,counts_7ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Amplitude = 7", fontsize=18)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True)  
plt.xlim(0,12500)                       #limits of x axis

plt.subplot(2, 2, 4)
plt.bar(ADC_channel_8ampl,counts_8ampl, width = ADC_channel_0ampl[1]-ADC_channel_0ampl[0])        
plt.title("Amplitude = 8", fontsize=18)           #title
plt.xlabel("ADC channels", fontsize=14)                        #xlabel
plt.ylabel("Counts", fontsize=14)              #ylabel
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)              #size of axis
plt.grid(True) 
plt.xlim(5000,max(ADC_channel_8ampl))                       #limits of x axis

plt.savefig('Spectra_shift_with_amplitude_LedDriver.png', format='png')
            
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 17:31:24 2018

@author: Jonny
"""

import matplotlib.pyplot as plt
import numpy as np
from FixedArrhenius import linearburialgraph, suddenupliftburialgraph, inversionburialgraph
'''
def linearburialgraph(time, tstep, A, E, burial, grad, tsurf, R = 8.314):
    oil = []
    RO = 1 #original oil in rock
    for t in np.arange(0, time, tstep):
        RT = RO*np.exp(-tstep*A*np.exp(-E/(R*lineartempfunction(burial, grad, t, tsurf)))) #where X = Rt/R0, assuming R0 = 1
        #perhaps can cheat - don't actually need to use t2-t1, because thats essentially tstep
        oil.append(RO*(1-(RT/RO))) #oil contains a list of ratios
        RO = RT #same as RO = RT/RO, because RO = 1
        #print(oil[-1])
    totaloil = np.cumsum(oil)
    #for i in range(len(totaloil)):
    #    print(totaloil[i])
    return totaloil
'''

''' #Previous CLN parameters
A1 = 3.16*10**15 #chloronapthalene params
E1 = 82874
R = 8.314
'''
A1 = 7.56*10**17 #chloronapthalene params
E1 = 106560.538
R = 8.314




#%%

### Basic Chloronapthalene Calculations ###

time = 3800 #Time modelled in Ma
tstep = 4 #Time interval between iterations in Ma
tsurf = 223 #Surface Temperature
tsurf2 = 273 #Surface Tempature for second graph (if needed)
burial = 10 #Burial Rate in m/Ma
grad = 0.02 #Geothermal Gradient in K/m
grad2 = 0.008
tuplift = 200 #Time at which the system begins to be exposed

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
#ax3 = fig.add_subplot(133)
ax1.plot(np.arange(0, time, tstep), linearburialgraph(time, tstep, A1, E1, burial, grad, tsurf, tuplift), 
         label='Linear\nBR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf)+' K')
ax1.plot(np.arange(0, time, tstep), suddenupliftburialgraph(time, tstep, A1, E1, burial, grad, tsurf, tuplift), 
         label='Sudden\nBR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf)+' K')
ax1.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, burial, grad, tsurf, tuplift), 
         label='Inversion\nBR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf)+' K')
#ax1.plot(np.arange(0, time, tstep), linearburialgraph(time, tstep, A1, E1, 300, grad, tsurf),
#         label='BR: 300 m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf)+' K')

ax2.plot(np.arange(0, time, tstep), linearburialgraph(time, tstep, A1, E1, burial, grad, tsurf2, tuplift),
         label='Linear\nBR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf2)+' K')
ax2.plot(np.arange(0, time, tstep), suddenupliftburialgraph(time, tstep, A1, E1, burial, grad, tsurf2, tuplift),
         label='Sudden\nBR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf2)+' K')
ax2.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, burial, grad, tsurf2, tuplift), 
         label='Inversion\nBR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf2)+' K')

'''
ax2.plot(np.arange(0, time, tstep), linearburialgraph(time, tstep, A2, E2, burial, grad, tsurf),
         label='BR: '+str(burial)+' m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf)+' K')
ax2.plot(np.arange(0, time, tstep), linearburialgraph(time, tstep, A2, E2, 300, grad, tsurf),
         label='BR: 300 m/Ma\nGG: '+str(grad)+' K/m\nST: '+str(tsurf)+' K')
'''
ax1.set_xlabel('Years / Ma')
ax2.set_xlabel('Years / Ma')
ax1.set_ylabel('% Lipids Lost')
ax1.set_ylim(0,1)
ax1.set_xlim(0, time)
ax2.set_ylim(0,1)
ax2.set_xlim(0, time)
ax1.set_title('Time of Uplift - '+str(tuplift)+' Ma after burial\nTotal time buried - '+str(2*tuplift)+' Ma\nMax Depth: '+str(burial*tuplift)+'m')
ax2.set_title('Time of Uplift - '+str(tuplift)+' Ma after burial\nTotal time buried - '+str(2*tuplift)+' Ma\nMax Depth: '+str(burial*tuplift)+'m')
ax1.legend(loc='lower right')
ax2.legend(loc='lower right')
plt.tight_layout()
plt.show()

#%%

##Variation of dechlorination with surface temperature

tstep = 4
maxdepth = [1000,2000,3000]
tsurf = [223,233,243,253,263,273]
time = 3800 #use 3800 for full model
grad = 0.02 #Geothermal Gradient in K/m
grad2 = 0.008
tuplift = 200 #Time at which the system begins to be exposed


#fig = plt.figure()
nrow = 2 #number of rows in final graph
ncol = 3 #number of columns in final graph

fig, axs = plt.subplots(nrow,ncol)

colours = ['#253494','#2c7fb8','#41b6c4','#fecc5c','#fc8d59','#d73027']

for i, ax in enumerate(fig.axes):
    if i<=2:
        for j in range(len(tsurf)): #each graph will have a line for each Surface Temperature from 223 to 273
            ax.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, maxdepth[i]/tuplift, grad, tsurf[j], tuplift), #burial = maxdepth[i]/tuplift
                     color = colours[j], label='ST: '+str(tsurf[j])+' K')
            ax.set_title('Max Depth: '+str(maxdepth[i])+'m, BR: '+str(maxdepth[i]/tuplift)+' m/Ma, GG: '+str(grad)+' K/m', fontsize=12, weight='bold')
            #ax.set_xlabel('Years / Ma')
            ax.set_ylabel('% 1-Chloronapthalene Lost', fontsize=12)
            ax.set_ylim(0,1)
            ax.set_xlim(0, time)
            yticks = ax.get_yticks()
            ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in yticks]) #changes the y-axis to %-ages
            
            if i == 2:
                # Shrink current axis by 20%
                box = ax.get_position()
                ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
                
                # Put a legend to the right of the current axis
                ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            
            #ax.legend(loc='lower right')

    else:
        for j in range(len(tsurf)):
            ax.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, maxdepth[i-3]/tuplift, grad2, tsurf[j], tuplift), 
                     color = colours[j], label='ST: '+str(tsurf[j])+' K')
            ax.set_title('Max Depth: '+str(maxdepth[i-3])+'m, BR: '+str(maxdepth[i-3]/tuplift)+' m/Ma, GG: '+str(grad2)+' K/m', fontsize=12, weight='bold')
            ax.set_xlabel('Years / Ma', fontsize=12)
            ax.set_ylabel('% 1-Chloronapthalene Lost', fontsize=12)
            ax.set_ylim(0,1)
            ax.set_xlim(0, time)
            yticks = ax.get_yticks()
            ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in yticks]) #changes the y-axis to %-ages
            
            if i == 5:
                # Shrink current axis by 20%
                box = ax.get_position()
                ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
                
                # Put a legend to the right of the current axis
                ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                
            #ax.legend(loc='lower right')

plt.subplots_adjust(top=0.925,
bottom=0.05,
left=0.04,
right=0.92,
hspace=0.275,
wspace=0.2)
plt.show()

#%%

##Comparison of Noachian and Amazonian Conditions

time = 400 #time = 400 for both is best
time2 = 400
tstep = 0.4 #Time interval between iterations in Ma
tsurf = 273 #Surface Temperature
tsurf2 = 248 #Surface Tempature for second graph (if needed)
burial = [0,7.5,15] #Burial Rate in m/Ma
grad = 0.02 #Geothermal Gradient in K/m
grad2 = 0.008
tuplift = 200 #Time at which the system begins to be exposed

#fig = plt.figure()
nrow = 3 #number of rows in final graph
ncol = 2 #number of columns in final graph

fig, axs = plt.subplots(nrow,ncol)

for i, ax in enumerate(fig.axes):
    if i % 2 == 0: #this checks to see if i is fully divisible by 2
        ax.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, burial[int(i/2)], grad, tsurf, tuplift), label='Burial: '+str(burial[int(i/2)])+' m/Ma')
        ax.set_ylabel('% 1-CLN Lost', fontsize=12)
        ax.set_ylim(0,1)
        ax.set_xlim(0, time)
        ax.legend(loc='upper right')
        yticks = [0,.2,.4,.6,.8,1]
        ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in yticks]) #changes the y-axis to %-ages
        if i == 0:
            ax.set_title('Noachian Conditions\nSurface Temp: '+str(tsurf)+' K\nGeothermal Gradient: '+str(grad)+' K/m', fontsize=12, weight='bold')
        if i == 4:
            ax.set_xlabel('Years / Ma', fontsize=12)
        
    else:
        ax.plot(np.arange(0, time2, tstep), inversionburialgraph(time2, tstep, A1, E1, burial[int(i/2)], grad2, tsurf2, tuplift), label='Burial: '+str(burial[int(i/2)])+' m/Ma')
        ax.set_ylim(0,1)
        ax.set_xlim(0, time2)
        yticks = [0,.2,.4,.6,.8,1]
        ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in yticks]) #changes the y-axis to %-ages
        ax.legend(loc='upper right')
        if i == 1:
            ax.set_title('Amazonian Conditions\nSurface Temp: '+str(tsurf2)+' K\nGeothermal Gradient: '+str(grad2)+' K/m', fontsize=12, weight='bold')
        if i == 5:
            ax.set_xlabel('Years / Ma', fontsize=12)
            
plt.show()

#%%

##FOR PAPER - What is the max burial depth given certain conditions##

time = 3800 #Time modelled in Ma
tstep = 4 #Time interval between iterations in Ma
tsurf = 273 #Surface Temperature
#tsurf2 = 273 #Surface Tempature for second graph (if needed)
maxdepth = [0,1000,2000,3000]
burial = 10 #Burial Rate in m/Ma
grad = 0.020 #Geothermal Gradient in K/m
grad2 = 0.008
tuplift = [1,100,200,300] #Time in Ma at which the system begins to be exposed

fig = plt.figure()
ax1 = fig.add_subplot(111)

for i in range(len(maxdepth)):
    ax1.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, maxdepth[i]/tuplift[i], grad, tsurf, tuplift[i]), label='Max Burial: '+str(maxdepth[i])+' m', linewidth = 2)
    
ax1.set_xlabel('\nYears / Ma', fontsize=20)
ax1.set_ylabel('% 1-CLN Lost\n', fontsize=20)

ax1.set_ylim(0,1)
ax1.set_xlim(0, time)
#ax1.set_title('Simulation of Burial under Noachian Conditions\n', fontsize=20, weight='bold')
#ax1.set_title('Time of Uplift - '+str(tuplift)+' Ma after burial\nTotal time buried - '+str(2*tuplift)+' Ma\nSurface Temp: '+str(tsurf)+' K, Geothermal Gradient: '+str(grad)+' K/m', fontsize=20, weight='bold')


yticks = ax1.get_yticks()
ax1.set_yticklabels(['{:3.0f}%'.format(x*100) for x in yticks]) #changes the y-axis to %-ages

plt.setp(ax1.get_xticklabels(), fontsize=14)
plt.setp(ax1.get_yticklabels(), fontsize=14)

plt.text(0.84, 0.02, 'Burial Rate: '+str(burial)+' m/Ma\nSurface Temp: '+str(tsurf)+' K\nGeothermal Gradient: '+str(grad)+' K/m', fontsize=12, bbox=dict(facecolor='red', alpha=0.2), horizontalalignment='center', verticalalignment='baseline', transform=ax1.transAxes)

# Shrink current axis by 20%
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
                
# Put a legend to the right of the current axis
ax1.legend(loc='center left', prop={'size': 12}, bbox_to_anchor=(1, 0.5))
#ax1.legend(loc='lower right')
plt.tight_layout()
plt.show()

#%%

##FOR PAPER - Attempt to find minimum age of CLN - Doesn't work!##

time = [200,400,600,800,3000] #Time modelled in Ma
tstep = 2 #Time interval between iterations in Ma
tsurf = 248 #Surface Temperature
#tsurf2 = 273 #Surface Tempature for second graph (if needed)
burial = 10 #Burial Rate in m/Ma
grad = 0.014 #Geothermal Gradient in K/m
grad2 = 0.008
tuplift = 100 #Time at which the system begins to be exposed

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

for i in range(len(time)):
    ax1.plot(np.arange(0, time[i], tstep), linearburialgraph(time[i], tstep, A1, E1, burial, grad, tsurf, tuplift), label='Time Modelled: '+str(time[i])+' Ma')

for i in range(len(time)):
    ax2.plot(np.arange(0, time[i], tstep), suddenupliftburialgraph(time[i], tstep, A1, E1, burial, grad, tsurf, tuplift), label='Time Modelled: '+str(time[i])+' Ma')

ax1.set_xlabel('Years / Ma')
ax1.set_ylabel('% 1-CLN Lost')
ax1.set_ylim(0,1)
ax1.set_xlim(0, max(time))
ax1.set_title('Linear Burial\nTime of Uplift - '+str(tuplift)+' Ma after burial\nTotal time buried - '+str(2*tuplift)+' Ma\nSurface Temp: '+str(tsurf)+' K, Geothermal Gradient: '+str(grad)+' K/m')
ax2.set_xlabel('Years / Ma')
ax2.set_ylabel('% 1-CLN Lost')
ax2.set_ylim(0,1)
ax2.set_xlim(0, max(time))
ax2.set_title('Sudden Uplift\nTime of Uplift - '+str(tuplift)+' Ma after burial\nTotal time buried - '+str(2*tuplift)+' Ma\nSurface Temp: '+str(tsurf)+' K, Geothermal Gradient: '+str(grad)+' K/m')
# Shrink current axis by 20%
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
                
# Put a legend to the right of the current axis
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#ax1.legend(loc='lower right')
#plt.tight_layout()
plt.show()
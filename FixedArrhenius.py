# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:30:25 2018

@author: Jonny
"""

import matplotlib.pyplot as plt
import numpy as np


##   LINEAR TEMPERATURE FUNCTION   ### Linear burial until a certain time, then reactant is held at the final temperature
def lineartempfunction(burialrate, geothermalgradient, time, tsurf, tuplift): #this is essentially the burial function
    if time <= tuplift:
        T = tsurf+burialrate*geothermalgradient*time #basic linear function
    else:
        T = tsurf+burialrate*geothermalgradient*tuplift
    return T

### SUDDEN UPLIFT TEMPERATURE FUNCTION ### Linear burial until a certain time, then reactant is immediately returned to the surface
def suddenuplifttempfunction(burialrate, geothermalgradient, time, tsurf, tuplift): #this is essentially the burial function
    if time <= tuplift:
        T = tsurf+burialrate*geothermalgradient*time #basic linear function
    else: 
        T = tsurf
    return T

### SLOW EXPOSURE TEMPERATURE FUNCTION ### Linear burial until a certain time, then reactant is slow returned to the surface - if not specified, the upliftrate == burialrate
def inversiontempfunction(burialrate, geothermalgradient, time, tsurf, tuplift, upliftrate = None):
    if upliftrate == None:
        upliftrate = burialrate
    if time <= tuplift: 
        T = tsurf + burialrate*geothermalgradient*time
    elif burialrate*geothermalgradient*tuplift - upliftrate*geothermalgradient*(time-tuplift) > 0: #this is an important step because otherwise the temperatures will go lower than the surface temperature
        T = tsurf + burialrate*geothermalgradient*tuplift - upliftrate*geothermalgradient*(time-tuplift) 
    else:
        T = tsurf
    return T

#%%
def linearburialgraph(time, tstep, A, E, burial, grad, tsurf, tuplift, R = 8.314):
    oil = []
    RO = 1 #original oil in rock
    for t in np.arange(0, time, tstep):
        if RO == 0 or t == 0:
            oil.append(0) #No oil can come out when there's nothing left, or at t = 0
        else:
            RT = RO*np.exp(-tstep*A*np.exp(-E/(R*lineartempfunction(burial, grad, t, tsurf, tuplift)))) 
            oil.append(RO*(1-(RT/RO))) #this expression appends the amount of oil released at this time step to list
            RO = RT #set original oil in rock to be remaining oil for next time step
    totaloil = np.cumsum(oil)
    return totaloil

def suddenupliftburialgraph(time, tstep, A, E, burial, grad, tsurf, tuplift, R = 8.314):
    oil = []
    RO = 1 #original oil in rock
    for t in np.arange(0, time, tstep):
        if RO == 0 or t == 0:
            oil.append(0)
        else:
            RT = RO*np.exp(-tstep*A*np.exp(-E/(R*suddenuplifttempfunction(burial, grad, t, tsurf, tuplift)))) #where X = Rt/R0, assuming R0 = 1
            oil.append(RO*(1-(RT/RO))) #oil contains a list of ratios
            RO = RT
    totaloil = np.cumsum(oil)
    return totaloil
       
def inversionburialgraph(time, tstep, A, E, burial, grad, tsurf, tuplift, upliftrate = None, R = 8.314):
    oil = []
    RO = 1 #original oil in rock
    for t in np.arange(0, time, tstep):
        if RO == 0 or t == 0:
            oil.append(0)
        else:
            RT = RO*np.exp(-tstep*A*np.exp(-E/(R*inversiontempfunction(burial, grad, t, tsurf, tuplift, upliftrate)))) #where X = Rt/R0, assuming R0 = 1
            oil.append(RO*(1-(RT/RO))) #this expression appends the amount of oil released at this time step to list
            RO = RT
    totaloil = np.cumsum(oil)
    return totaloil
#%%

'''
#Example Use of Code for Graph Construction

A1 = 5.7*10**26 #Frequency factor in units of Ma**-1
E1 = 218250 #Activation Energy in units of J/Mol
burial = 308.4 #Rate of burial per Ma
grad = 0.0474 #Geothermal Gradient in K/m
tsurf = 298 #Surface Temperature
time = 15 #Length of simulated burial in Ma
tstep = 0.2 #Time intervals for calculation (smaller = more resolution, longer computational time)
tuplift = 8 #Time at which any burial stops and uplift occurs

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(np.arange(0, time, tstep), linearburialgraph(time, tstep, A1, E1, burial, grad, tsurf, tuplift), label = 'Linear Burial', linewidth=2)
ax1.plot(np.arange(0, time, tstep), suddenupliftburialgraph(time, tstep, A1, E1, burial, grad, tsurf, tuplift), label='Sudden Uplift', linewidth=2)
ax1.plot(np.arange(0, time, tstep), inversionburialgraph(time, tstep, A1, E1, burial, grad, tsurf, tuplift), label = 'Inversion', linewidth=2)

#ax2.plot(np.arange(520, 0, -4), cratonburialgraph(A1, E1, R, t=520), color='k')
#ax2.plot(np.arange(0, 520, 4), cratonburialgraph(520, 4, A1, E1, 12.2, 0.0328, tsurf, tuplift=280))
ax1.legend(loc='upper left')
ax1.set_ylim(0,1)
ax1.set_xlim(0, time)
ax2.set_ylim(0,1)
ax2.set_xlim(0, 520)
plt.show()
'''


#%%
'''
##   LINEAR TEMPERATURE FUNCTION   ###
def lineartempfunction(burialrate, geothermalgradient, time, tstep, tsurf): #this is essentially the burial function
    for t in np.arange(0, time, tstep):
        T = tsurf+burialrate*geothermalgradient*t #basic linear function
    return T


def suddenuplifttempfunction(burialrate, geothermalgradient, time, tstep, tsurf, tuplift): #this is essentially the burial function
    for t in np.arange(0, time, tstep):
        if t <= tuplift:
            T = tsurf+burialrate*geothermalgradient*t #basic linear function
        else: 
            T = tsurf
    return T

def burialgraph(time, tstep, A, E, burial, grad, tsurf, T, tuplift, R = 8.314):
    oil = []
    RO = 1 #original oil in rock
    for t in np.arange(0, time, tstep):
        if T == 'linear':
            temp = lineartempfunction(burial, grad, t, tsurf)
        if T == 'sudden':
            temp = suddenuplifttempfunction(burial, grad, t, tsurf, tuplift)
        RT = RO*np.exp(-tstep*A*np.exp(-E/(R*temp))) #where X = Rt/R0, assuming R0 = 1
        #perhaps can cheat - don't actually need to use t2-t1, because thats essentially tstep
        oil.append(RO*(1-(RT/RO))) #oil contains a list of ratios
        RO = RT #same as RO = RT/RO, because RO = 1
        #print(oil[-1])
    totaloil = np.cumsum(oil)
    #for i in range(len(totaloil)):
    #    print(totaloil[i])
    return totaloil
'''
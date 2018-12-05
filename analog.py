##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Wed Dec  5 15:02:55 2018
#
#@author: guttappa
#"""
#importing the dependencies
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
##importing the sound file
x1, fs = sf.read('g1.wav')
##assigning the frequencies
f1=5
f2=100
f3=1000000
f4=1
####creating time vectors
t1= np.arange(0,2,0.001)
t2= np.arange(0,0.1,0.001)
t3= np.arange(0,0.0001,0.00000001)
t4= np.arange(0,(len(x1))/fs,1/fs)
##creating the sinewaves
x2=np.sin(2*np.pi*f1*t1)
x3=np.sin(2*np.pi*f2*t2)
x4=np.sin(2*np.pi*f3*t3)
x5=np.sin(2*np.pi*f4*t4)
##adding sinewave to the audio signal
z=x1+x5

###plotting the all graphs 
plt.subplot(6,1,1)
plt.plot(t1,x2)
plt.subplot(6,1,2)
plt.plot(t2,x3)
plt.subplot(6,1,3)
plt.plot(t3,x4)
plt.subplot(6,1,4)
plt.plot(t4,x1)
plt.subplot(6,1,5)
plt.plot(t4,z)
######
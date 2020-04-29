import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 100.0;  # sampling rate
Ts = 10.0/Fs; # sampling interval
t = np.arange(0,10,Ts) # time vector; create Fs samples between 0 and 1.0 sec.
x = np.arange(0,10,Ts) # signal vector; create Fs samples
y = np.arange(0,10,Ts) # signal vector; create Fs samples
dis = np.arange(0,10,Ts) # signal vector; create Fs samples
tilt = np.arange(0,10,Ts) # signal vector; create Fs samples

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
#line=s.readline() # Read an echo string from K66F terminated with '\n'

for i in range(0, int(Fs)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    #x[i] = float(line.decode('utf-8'))
    x[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    #y[i] = float(line.decode('utf-8'))
    y[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    #z[i] = float(line.decode('utf-8'))
    dis[i] = float(line)
    #line=s.readline()
    #tilt[i] = int(line)

#print(x)
"""for i in range(0, 100):
    if (z[i] < 0.7):
        tilt[i] = 1.0
    else :
        tilt[i] = 0
"""
fig, ax = plt.subplots(2, 1)
#fig = plt.figure()
#ax[0] = plt.subplots(211)
#ax[1] = plt.subplots(212)
#plt.subplots(211)
ax[0].plot(t,x, color = "blue", label = "x")
ax[0].plot(t,y, color = "red", label = "y")
#ax[0].plot(t,z, color = "green", label = "z")
ax[0].legend(loc='lower left') # show x y z label 
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
#fig, ax = plt.subplots(212)
#plt.subplots(212)
"""for i in range(0, 100) :
    ax[1].plot([i/10, i/10], [0, tilt[i]], color = 'blue',) #[x,x1] , [y,y1] -> x,y to x1,y1
    ax[1].scatter([i/10,], [tilt[i],], 40, color = 'blue') # put point
"""
ax[1].plot(t,dis, color = "red",)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('displacemant')
plt.show()

s.close()

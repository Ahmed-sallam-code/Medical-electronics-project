import FFT_Sallam as freq
import numpy as np 
import time
import com_ard as com
com.get_serial()
print("data collected, getting ready to apply the fourier transform")
sr = len(com.acceleration_listx)/10
t = np.arange(0,10,10/(len(com.acceleration_listx)))
s=com.accel_listx()
for i in range(len(s)):   
    try:  
        s[i]=float(s[i])
    except:
        print("Error encountered, couldn't covert to float")
        s[i]=(float(s[i-10])+float(s[i+10]))/2


d=com.accel_listy()
for i in range(len(d)):   
    try:  
        d[i]=float(d[i])
    except:
        d[i]=(float(d[i-10])+float(d[i+10]))/2
        print("Error encountered, couldn't covert to float")

f=com.accel_listz()
for i in range(len(f)):   
    try:  
        f[i]=float(f[i])
    except:
        f[i]=(float(f[i-10])+float(f[i+10]))/2
        print("Error encountered, couldn't covert to float")        

freq.plot_fft(s,sr,t,"Frequency(hz)","time(s)","amplitude x","amplitude")
freq.plot_fft(d,sr,t,"Frequency(hz)","time(s)","amplitude y","amplitude")
freq.plot_fft(f,sr,t,"Frequency(hz)","time(s)","amplitude z","amplitude")
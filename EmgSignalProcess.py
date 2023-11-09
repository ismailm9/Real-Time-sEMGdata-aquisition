'''
Signal processing and feature exraction for 8-channel EMG raw data
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, firwin, lfilter
from scipy import signal
import csv
import openpyxl
from scipy.stats import kurtosis, skew, entropy
import peakutils
import math

def SignalProcess(part,hand):
    
    load_emg(channel[8],marker)
    
    emgdatas = [Emg0,Emg1,Emg2,Emg3,Emg4,Emg5,Emg6,Emg7]
  
   
    screen_size = (16, 9)
    
    fig = plt.figure(hand+" Feats",figsize=screen_size)
    
    fig.suptitle(hand+' Feats') 
    
    
    for d in range(len(emgdatas)):
        
        df1_cropped = df1.iloc[:]
        
        timestamp = pd.to_datetime(df1_cropped['TimeE'])
        
        ts = pd.Series(emgdatas[d][:].values, index=timestamp)

        # EMG signal filtering
        fs = 170  # Sample frequency (Hz)
        
        lowcut1 = 0.01  # low-cutoff (Hz)
        
        highcut1 = 0.012 # high-cutoff (Hz)
        
        lowcut = 0.035  # low-cutoff (Hz)
        
        highcut = 0.155 # high-cutoff (Hz)
      
        order = 3  # filter order
        
        frame= 150 # sliding window
        
        step = 25 #sliding step
        
        filtdata=filter_notch(ts)
        
        filtdata1=filter_bandpass(filtdata)
        
        #Signal rectification
        rectified_data = np.absolute(filtdata1)
        
        smoothed_data = rectified_data
        
        mnp = []
        tot = []
        mnf = []
        rms = []
        var = []
        mav = []
        iemg = []
        wa = []
        kurt = []
        skewness = []
        entrop = []


        # Marker_Points and Features extraction
        markerpoints=markermapping(frame,marker.size, step)
        
        th = np.mean(smoothed_data) + 3 * np.std(smoothed_data)
        
        for i in range(frame, smoothed_data.size, step):
            
                x = smoothed_data[i - frame:i]
                            
                difff = np.diff(smoothed_data)
                
                rms.append(np.sqrt(np.mean(np.square(x))))
                
                var.append(np.var(x,ddof=0))
                
                mav.append(np.sum(np.abs(x))/frame)
                
                iemg.append(np.sum(np.abs(x)))
                
                wa.append(np.sum(abs(np.diff(x))))
                
                frequency, power = spectrum(x, fs)
                
                mnp.append(np.sum(power) / len(power))
                
                tot.append(np.sum(power))
                
                mnf.append(mean_freq(frequency, power))
                
                VAR=pd.DataFrame({'VAR':var})
                
                RMS=pd.DataFrame({'RMS':rms})
                
                IEMG=pd.DataFrame({'IEMG':iemg})
                
                MAV=pd.DataFrame({'MAV':mav})
                
                WL=pd.DataFrame({'WaveLength':wa})
                
                MNP=pd.DataFrame({'MeanPower':mnp})
                
                TOTL=pd.DataFrame({'TotalPower':tot})
                
                MNF=pd.DataFrame({'MeanFreq':mnf})
                
                           
        write_csv(dataemg_features, markerpoints):
            
            writer = csv.writer(dataemg)
            
            writer.writerow(['VAR', 'RMS', 'IEMG', 'MAV', 'WAMP', 'MNP', 'TOTL', 'MNF'])
            
            for row in zip(var, rms, iemg, mav, wa, mnp, tot, mnf):
                
                writer.writerow(row)
                
                writer.writerow(markerpoints)

        emglbl = ['Emg0', 'Emg1', 'Emg2', 'Emg3', 'Emg4', 'Emg5', 'Emg6', 'Emg7','Marker']
        
        plot_features(6,2,markerpoints)
        
    plt.tight_layout()
    
    fig.subplots_adjust(hspace=0.35, wspace=0.185, bottom=0.065, top=0.960, left=0.059, right=0.983,)
    
    plt.show()


    

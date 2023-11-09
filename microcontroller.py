"""
sEMG data write to CSV from Microcontroller 8-channel ADC
"""

import time
import serial
import pandas as pd
from datetime import datetime
import csv
import re

def dataemg(participant,handpose,dra,comPort):
    
    print('EMG Recording')
    
    microcontroller = serial.Serial(port=comPort, baudrate=115200, timeout=0.1)
    
    header = ['TimeE','Emg0','Emg1','Emg2','Emg3','Emg4','Emg5','Emg6','Emg7','Marker','Label']
    
    create_csv(header, name)
    
    runtime(duration=35)
    
    while (time.time() - start_time) <duration:
        
        emg1 = microcontroller.readline()
        
        emg11=emg1.decode('utf-8').rstrip()
        
        numbers_string_list = re.findall(r'\d+', emg11)
        
        emg11 = [int(num) for num in numbers_string_list]
        
        tm=datetime.now()
        
        timetime=datetime.strftime(tm,'%H:%M:%S.%f')[:]
        
        datae=[timetime,*emg11, 0, handpose]#0:Open, 1:Fist,  2:Tumb, 3:Index, 4:Middle, 5:Ring, 6:Pinky handposes from camera finger_identicate() algorithm
        
        write_csv(datae)
        
    print('EMG Recorded')

    
    
    
    
    
    
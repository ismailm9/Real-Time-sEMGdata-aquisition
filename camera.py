'''
Directing the 3-second on and 3-second off operations by writing them on the screen
by determining finger movements with the camera. Ability to create a marker line on the signal
by placing 1 marker at each opening and closing transition. It is saved to the same csv file as emg.
'''
import cv2 
from datetime import datetime
from cvzone.HandTrackingModule import HandDetector
import csv
import time
from datetime import datetime


def camcam(bmi,kolw,kolc,gndr,participant,dra,camPort):   
   
    cap = cv2.VideoCapture(camPort)
 
    detector=HandDetector(detectionCon=0.8)

    header = ['TimeE','Emg0','Emg1','Emg2','Emg3','Emg4','Emg5','Emg6','Emg7','Marker','Label']
    
    create_csv(header, name)
    
    runtime(duration=35)
    
    while (time.time() - start_time) < duration:
        
        HandDetector(HandTracking)
        
        send_marker_to_csv(1, status=1, 0, status=0, sec=3)              
       
        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # 21 landmarks
            
            find_distance_finger([tumb,index,middle,ring,pinky], eucledian)

            fingers1 = detector.fingersUp(hand1)
            totalFingers = fingers1.count(1)
            
            dst = {'Tumb':tumb,'Index':index,'Middle': middle, 'Ring':ring, 'Pinky':pinky}                
            
            finger_identicate(fingers1=5,"Open", fingers1=0,"Fist", fingers1=4,[minfinger(dist)])
        
        write_csv(marker, fingers1)
                           
        cv2.imshow("Image", img)
        
        k=cv2.waitKey(100) & 0xff
        
        if k==27:            
            break
    
    cv2.destroyAllWindows()
    cap.release()

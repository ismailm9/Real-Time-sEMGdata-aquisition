'''
Human-Computer Interaction (HCI) interface
'''

from threading import Thread
import customtkinter
from tkinter import *
import camera
from serial.tools.list_ports import comports
from EmgSignalProcess import SignalProcess
import microcontroller


customtkinter.set_appearance_mode("dark")  #"System", "Dark", "Light"
customtkinter.set_default_color_theme("green")  # "blue", "green", "dark-blue"


def NormF():
    actionName=["Fist","Tumb","Index","Middle","Ring","Pinky"]
    hand=actionName[action_var.get()]
    part=partic.get()    
    NORMF(part)

def Normalize():
    part=partic.get()    
    NORM(part)
    
def sp():
    actionName=["Fist","Tumb","Index","Middle","Ring","Pinky"]
    hand=actionName[action_var.get()]
    part=partic.get()    
    SignalProcess(part,hand)

def pth():
    gen=gender_var.get()
    pers=partic.get()
    PredictionToHand(gen,pers)
    
    
def getSignal():
    actionName=["_Fist-Open","_Tumb-Open","_Index-Open","_Middle-Open","_Ring-Open","_Pinky-Open"]
    gndr=gender_var.get()
    handpose=action_var.get()
    
    par=partic.get()
    dra=duration.get()
    print(gndr)
    print(handpose)
    participant=""
    for t in par:
        participant+=str(t)
    participant+=actionName[handpose]
    camPort=int(ccB.get())
    comPort=acB.get()[-5:-1]
    
    bmi=""
    a=age.get()
    for t in a:
        bmi+=str(t)
    k=armc.get()
    kolc="" 
    for t in k:
        kolc+=str(t)
    kw=armw.get()
    kolw=""
    for t in kw:
        kolw+=str(t)  
    try:
        if p=="":
            messagebox.showinfo("Warning","Volunteers number!")
            return 0
    except  :
        pass
    
    
    t1 = Thread(target=camera.camcam, args=(bmi,kolw,kolc,gndr,participant,dra,camPort))
    t2 = Thread(target=microcontroller.dataemg, args=(participant,handpose,dra,comPort))
    t1.start()
    t2.start()
    t1.join()
    t2.join()     

  
app = customtkinter.CTk()
app.geometry("1300x600")
app.resizable(width=FALSE, height=FALSE)
app.title("Real-Time Data Aquisition")

frame_Header = customtkinter.CTkFrame(master=app,
                  height=60,
                  corner_radius=10)
frame_Header.pack(pady=5, padx=20,fill="x")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=5, padx=20, fill="both")
frame_input=customtkinter.CTkFrame(master=frame_1,width=150,height=75)
frame_input.pack(pady=20, padx=20, fill="both",side="left")
Gender=customtkinter.CTkFrame(master=frame_1,width=150,height=150)
Gender.pack(pady=20, padx=20, fill="both",side="left")
frame_button=customtkinter.CTkFrame(master=frame_1,width=150,height=150)
frame_button.pack(pady=20, padx=20, fill="both", side="left")
frame_device=customtkinter.CTkFrame(master=frame_1,width=150,height=150)
frame_device.pack(pady=20, padx=20, fill="both",side="left")


baykus = customtkinter.CTkFrame(master=frame_Header)
baykus.pack(side='left',padx=10, pady=10)
backgnd = PhotoImage(file='background.png')
logo = PhotoImage(file='baykus156x120.png')
log = Label(master=baykus, image=logo, background="gray")
log.pack(side='left')

button_4 = customtkinter.CTkButton(master=frame_button, text="sEMG and Camera Data Recording", corner_radius=10,
                                   font=customtkinter.CTkFont(size=20, weight="bold"), border_spacing=5, fg_color="salmon",
                                   text_color="brown", hover_color=("green", "yellow"),compound='top',border_width=1, command=getSignal)
button_4.pack(side='top',padx=20, pady=10)


gender_var = customtkinter.IntVar()
action_var = customtkinter.IntVar()

genderLabel = customtkinter.CTkLabel(master=frame_input, text="Gender")
genderLabel.pack(side='top',padx=5, pady=5)
gender_1 = customtkinter.CTkRadioButton(master=frame_input, text="Female",
                                              variable= gender_var, value=1)
gender_2 = customtkinter.CTkRadioButton(master=frame_input, text="Male",
                                             variable= gender_var, value=0)
gender_1.pack(side='top',padx=10, pady=10)
gender_2.pack(side='top',padx=10, pady=10)

actionLabel = customtkinter.CTkLabel(master=Gender, text="Action")
action_1 = customtkinter.CTkRadioButton(master=Gender, text="Fist-Open",
                                             variable=  action_var, value=0)
action_2 = customtkinter.CTkRadioButton(master=Gender, text="Tumb-Open",
                                             variable=  action_var, value=1)
action_3 = customtkinter.CTkRadioButton(master=Gender, text="Index-Open",
                                             variable=  action_var, value=2)
action_4 = customtkinter.CTkRadioButton(master=Gender, text="Middle-Open",
                                             variable=  action_var, value=3)
action_5 = customtkinter.CTkRadioButton(master=Gender, text="Ring-Open",
                                             variable=  action_var, value=4)
action_6 = customtkinter.CTkRadioButton(master=Gender, text="Pinky-Open",
                                             variable= action_var, value=5)
actionLabel.pack()
action_1.pack(padx=10, pady=5)
action_2.pack(padx=20, pady=5)
action_3.pack(padx=30, pady=5)
action_4.pack(padx=40, pady=5)
action_5.pack(padx=50, pady=5)
action_6.pack(padx=60, pady=5)
acB=customtkinter.CTkComboBox(master=frame_device)
acB.pack(padx=20, pady=10,fill="x")#ipady=5,ipadx=40)
ports = comports()
values=[]
for port, desc, hwid in sorted(ports):
    values.append(desc)
    
acB.configure(values=values)
acB.set(values[0])
comPort=acB.get()[-5:-1]

ccB=customtkinter.CTkComboBox(master=frame_device)
ccB.pack(padx=20, pady=10, fill="x")#,ipady=5,ipadx=40)
index = 0
arr = ""
videoList=["0","1"]


ccB.configure(values=videoList)
ccB.set(videoList[0])

button_4 = customtkinter.CTkButton(master=frame_device, text="Normalization Full", corner_radius=10,
                                   font=customtkinter.CTkFont(size=25, weight=None), border_spacing=5, fg_color="blue",
                                   text_color="salmon", hover_color=("green", "green"),border_width=1,command=NormF)
button_4.pack(side='top',padx=20, pady=1)

button_5 = customtkinter.CTkButton(master=frame_device, text="Prediction to Hand", corner_radius=10,
                                   font=customtkinter.CTkFont(size=25, weight=None), border_spacing=5, fg_color="blue",
                                   text_color="salmon", hover_color=("green", "green"),border_width=1,command=pth)
button_5.pack(side='top',padx=20, pady=1)

button_6 = customtkinter.CTkButton(master=frame_button, text="sEMG Signal Processing and Feature Extraction",  corner_radius=10,
                                   font=customtkinter.CTkFont(size=15, weight="bold"), border_spacing=5, fg_color="salmon",
                                   text_color="brown", hover_color=("green", "yellow"),command=sp)
button_6.pack(side='top',padx=20, pady=1)

label_1 = customtkinter.CTkLabel(master=frame_Header, text="Classification of hand-finger gestures with machine learning algorithm using sEMG sensor and camera image data", corner_radius=10, fg_color="brown", text_color=("red", "thistle3"), font=customtkinter.CTkFont(size=20, weight="bold"))
label_1.pack(side='top',padx=20, pady=10)

armw=customtkinter.CTkEntry(master=frame_input, corner_radius=10, placeholder_text="Forearm Length",
                            placeholder_text_color="black",  height=30, border_width=5, fg_color="wheat", text_color="red")
armw.pack(side='bottom',padx=20, pady=10)

armc=customtkinter.CTkEntry(master=frame_input, corner_radius=10, placeholder_text="Forearm Perimeter",
                            placeholder_text_color="black",  height=30, border_width=5, fg_color="wheat", text_color="red")
armc.pack(side='bottom',padx=20, pady=10)

age=customtkinter.CTkEntry(master=frame_input, corner_radius=10, placeholder_text="Participant BMI",
                           placeholder_text_color="black",  height=30, border_width=5, fg_color="wheat", text_color="red")
age.pack(side='bottom',padx=20, pady=10)

partic=customtkinter.CTkEntry(master=frame_input, corner_radius=10, placeholder_text="Participant No",
                              placeholder_text_color="black",  height=30, border_width=5, fg_color="wheat", text_color="red")
partic.pack(side='bottom',padx=20, pady=10)

duration=customtkinter.CTkEntry(master=frame_input, corner_radius=10, placeholder_text="RecTime Def=35sn",
                              placeholder_text_color="black",  height=30, border_width=5, fg_color="wheat", text_color="red")
duration.pack(side='bottom',padx=20, pady=10)
app.mainloop()

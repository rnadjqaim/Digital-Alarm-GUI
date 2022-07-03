from tkinter import *
import time
import datetime
import winsound
from threading import * 

win = Tk ()
win.geometry ("400x600")

def Thred1 () :
    t1 = Thread(target =alarming)
    t1.start()

def alarming () :
    while True :
        # inf loop
        sett = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep (1)
        currentTime =datetime.datetime.now().strftime('%H:%M:%S')
        print (currentTime,sett)

        if sett == currentTime :
            print ("Time out ")

Label (win, text= 'alarm clock')
Label (win , text ="set time" )

frame = Frame (win)
frame.pack()

hour = StringVar (win)
hours =('00','01','03')
hour.set (hours[0])
hrs = OptionMenu(frame,hour,*hours)
hrs.pack()
#---------
minute =StringVar (win)
minutes = ('00','01','03')
minute.set(minutes[0])
mins = OptionMenu(frame,minute,*minutes)
mins.pack()
#-----------

second = StringVar (win)
seconds = ('00','01','03')
second.set (seconds[0])
secs =OptionMenu(frame,second,*seconds)
secs.pack()
Button (win, text ="alarm sets",command = Thred1).pack()
win.mainloop() 



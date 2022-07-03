from tkinter import *
import datetime
import time
from threading import *
# api

screen = Tk()
screen.geometry ("200x400")
screen.title ("Rnad_Alarm")
screen.config(background = "pink")
#screen.pack()

def threading_Rnad  () :
    t = Thread (target = RnadAlarm)
    t.start()

def RnadAlarm() :
    while True :
        time.sleep (1)
        set_time = f"{hour.get()}: {minute.get()}: {second.get()} "
        time.sleep (1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print ("current Time"+str(current_time))
        print (current_time)

        if set_time == current_time :
           print ("Time Out , please Wake up ! ")
Label (screen, text ='set your time, please' )
Label (screen, text ='current time, now !' )
screen.pack()

frame = Frame (screen )
frame.pack()

#hours
hour = StringVar(screen)
hours = ('00','01','02','03','04')
hour.set(hours[0])
hrs = OptionMenu (frame,hour,*hours)
hrs.pack()
#minute
minute = StringVar(screen)
minutes = ('00','01','02','03','04')
minute.set(minutes[0])
mins = OptionMenu (frame,minute,*minutes)
mins.pack()

#second
second = StringVar(screen)
seconds = ('00','01','02','03','04')
second.set(seconds[0])
secs= OptionMenu (frame,second,*seconds)
secs.pack()



c= Button (screen,text ='Alarm Set', command = threading_Rnad)
c.pack()
screen.mainloop()









    

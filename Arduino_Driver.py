#! /usr/bin/python3
# Arduino_Driver.py


import serial
import time
from tkinter import *

ArduinoSerial = serial.Serial('/dev/cu.usbmodem14101', 9600, timeout=.1) # open serial port
time.sleep(2)

def gas_on():
   ArduinoSerial.write(b'1') # set Arduino output pin 13 high
   var1.set(ArduinoSerial.readline().decode('utf-8').strip())# get Arduino output pin 13 status
   if var1.get() == '1':
       var1.set('Gas is running')

def gas_off():
   ArduinoSerial.write(b'0') # set Arduino output pin 13 low
   var1.set(ArduinoSerial.readline().decode('utf-8').strip()) # get Arduino output pin 13 status
   if var1.get() == '0':
       var1.set('Gas stopped')

def led_Exit():
   ArduinoSerial.write(b'0') # set Arduino output pin 13 low and quit
   ArduinoSerial.close() # close serial port
   quit()

root = Tk()

font1 = "-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
font2 = "-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"
font3 = "-family {@Arial Unicode MS} -size 12 -weight bold -slant roman -underline 1 -overstrike 0"
font4 = "-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

var1 = StringVar()
var1.set('OFF')
root.geometry("430x200+600+200")
root.title("                                         Arduino Output Control")
root.configure(background="#d9d9d9")


btn1 = Button(root, text='Gas valve: OPEN', font = font1, bg = 'light green', highlightbackground= 'black',   \
       borderwidth = 3, activebackground = 'light gray', relief=RAISED, command=gas_on) # activate Arduino pin 13
btn1.place(relx=0.34, rely=0.10, height=30, width=150)

btn2 = Button(root, text='Gas valve: CLOSED', font = font1, bg = 'red2', fg = 'white', highlightbackground= 'black',   \
       borderwidth = 3, activebackground = 'light gray', relief=RAISED, command=gas_off) # deactivate Arduino pin 13
btn2.place(relx=0.34, rely=0.30, height=30, width=150)

btn3 = Button(root, text='Exit', font = font3, bg = 'maroon1', highlightbackground= 'black',   \
       borderwidth = 3, activebackground = 'gray', relief=RAISED,command=led_Exit) # close serial port and quit program
btn3.place(relx=0.34, rely=0.50, height=30, width=150)

lbl1 = Label (root, textvariable = var1, font = font2, bg = 'light blue', fg = 'black', highlightbackground= 'black',   \
       borderwidth = 3, relief=RAISED) # message label for status of arduino pin 13
lbl1.place(relx=0.34, rely=0.70, height=30, width=150)

root.mainloop()
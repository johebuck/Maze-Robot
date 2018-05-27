import RPi.GPIO as GPIO
import time
import Tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

m11=16
m12=12
m21=21
m22=20

GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m12,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)
GPIO.setup(m22,GPIO.OUT)
time.sleep(5)

def stop():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)

def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)

def left():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)

def right():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def key_input(event):
    print 'Key:', event.char
    key_press=event.char
    sleep_time=0.30

    if key_press.lower()=='w':
        forward(sleep_time)
    elif key_press.lower()=='s':
        back(sleep_time)
    elif key_press.lower()=='a':
        left(sleep_time)
    elif key_press.lower()=='d':
        right(sleep_time)

command=tk.Tk()
command.bind('<KeyPress', key_input)
command.mainloop()
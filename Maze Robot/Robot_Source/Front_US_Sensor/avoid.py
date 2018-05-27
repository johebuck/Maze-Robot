import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 27
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m12,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)
GPIO.setup(m22,GPIO.OUT)



time.sleep(5)

def stop():
    print "stop"
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print "Forward"

def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print "back"

def left():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print "left"

def right():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    print "right"

stop()
count=0
while True:
 i=0
 avgDistance=0
 for i in range(5):
  GPIO.output(TRIG, False)
  time.sleep(0.1)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  pulse_start = time.time()
  pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150
  distance = round(distance,2)
  avgDistance=avgDistance+distance

 avgDistance=avgDistance/5
 print avgDistance
 flag=0
 if avgDistance < 15:
    count=count+1
    stop()
    time.sleep(1)
    back()
    time.sleep(1.5)
    if (count%3 ==1) & (flag==0):
     right()
     flag=1
    else:
     left()
     flag=0
    time.sleep(1.5)
    stop()
    time.sleep(1)
 else:
    forward()
    flag=0


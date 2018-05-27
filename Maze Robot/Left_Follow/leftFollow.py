import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG=17
ECHO1=27
ECHO2=26

m11=16
m12=12
m21=21
m22=20

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.setup(4, GPIO.IN)
GPIO.setup(19, GPIO.IN)

GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)

time.sleep(5)

def stop():
	print("stop")
	GPIO.output(m11, 0)
	GPIO.output(m12, 0)
	GPIO.output(m21, 0)
	GPIO.output(m22, 0)

def forward():
	print("forward")
	GPIO.output(m11, 1)
	GPIO.output(m12, 0)
        GPIO.output(m21, 1)
        GPIO.output(m22, 0)

def back():
	print("back")
	GPIO.output(m11, 0)
        GPIO.output(m12, 1)
        GPIO.output(m21, 0)
        GPIO.output(m22, 1)

def left():
	print("left")
	GPIO.output(m11, 0)
        GPIO.output(m12, 0)
        GPIO.output(m21, 1)
        GPIO.output(m22, 0)

def right():
	print("right")
	GPIO.output(m11, 1)
        GPIO.output(m12, 0)
        GPIO.output(m21, 0)
        GPIO.output(m22, 0)

stop()

print("Script Start")

while(True):
	GPIO.output(TRIG, True)
	time.sleep(0.1)
	GPIO.output(TRIG, False)
	
	start_ECHO1=time.time()
	stop_ECHO1=time.time()

	start_ECHO2=time.time()
	stop_ECHO2=time.time()

	while GPIO.input(ECHO1)==0:
		start_ECHO1=time.time()

	while GPIO.input(ECHO2)==0:
		start_ECHO2=time.time()

	while GPIO.input(ECHO1)==1:
		stop_ECHO1=time.time()

	while GPIO.input(ECHO2)==1:
		stop_ECHO2=time.time()

	TimeElapsed_ECHO1=stop_ECHO1-start_ECHO1
	distance_ECHO1=TimeElapsed_ECHO1*17150

	TimeElapsed_ECHO2=stop_ECHO2-start_ECHO2
	distance_ECHO2=TimeElapsed_ECHO2*17150

	front_sensor=distance_ECHO1
	left_sensor=distance_ECHO2

	if front_sensor>45 and left_sensor<0.5:
		forward()

	if front_sensor>45 and left_sensor>0.5:
		stop()
		time.sleep(0.1)
		right()

	if front_sensor<30 and left_sensor<0.5:
		stop()
		time.sleep(0.1)
		left()

	if front_sensor<30 and left_sensor>0.5:
		stop()
		time.sleep(0.1)
		left()

	if (GPIO.input(4)==0):
		back()
		time.sleep(0.5)
		left()
		time.sleep(0.2)

	if (GPIO.input(19)==0):
		back()
		time.sleep(0.5)
		right()
		time.sleep(0.2)

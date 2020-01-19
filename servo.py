import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50) #PIN 11, 50Hz pulse


servo1.start(0)
time.sleep(2)

duty = 2

while True==True:
	duty=float(input("Enter angle : ") )
	if duty >180:
		continue
	if duty <0:
		continue
		
	duty=2+(duty/18)
	print (duty)
	servo1.ChangeDutyCycle(duty)
	time.sleep(1)
	servo1.ChangeDutyCycle(0)


import socket

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50) #PIN 11, 50Hz pulse


servo1.start(0)
time.sleep(2)

duty = 2


#AF_INET = IPV4,
#SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.0.89', 1234))

while True:
#Buffer size
	msg = s.recv(10240)
	angle= msg.decode('utf-8')
	angle = float(angle)
	duty=2+(angle/18)
	print (duty)
	servo1.ChangeDutyCycle(duty)
	time.sleep(.1)

		
	

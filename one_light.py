from gpiozero import LED
import time
import time
import slack
import requests
import os
file ='blink_speed.txt'
def read_in_doc(file):
	file = open(file, "r") 
	return file.read() 

led=LED(18)
while True==True:
	try:
		blink_speed =float(read_in_doc(file)	)
	except:
		blink_speed=.01
		print (oops)
	led.on()
	time.sleep(blink_speed)
	led.off()
	time.sleep(blink_speed)

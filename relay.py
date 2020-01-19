from gpiozero import LED
import time
import time
import requests
import os

led=LED(18)
blink_speed=5
while True==True:
	led.on()
	time.sleep(blink_speed)
	led.off()
	time.sleep(blink_speed)

from gpiozero import LED
import time
import time
import requests
import os

blink_speed = 5

led=LED(18)

led.on()
time.sleep (200)
#Homework: if the user types in on turn the led if the user types off turn the led off and if the user types toggle make the led toggle

from machine import PIN
from time import sleep 
led = Pin (15, Pin.OUT)
while True: 
	CMD = input(‘What Do You Want the LED to Be “ON/OFF/TOGGLE”?’)
	print(CMD) 
	if CMD == “ON”:
		led.value (1)
	if CMD == “OFF”:
		led.value(0)
	if CMD == “TOGGLE”:
		led.toggle()


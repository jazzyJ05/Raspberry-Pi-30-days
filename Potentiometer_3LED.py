#Build a potentiometer that controls a red, green, yellow


from machine import PIN
from time import sleep 

potPin = 28
greenPin = Pin(13,Pin.OUT)
yellowPin = Pin(14,Pin.OUT)
redPin = Pin(15,Pin.OUT)
myPot = machine.ADC(potPin)

while True: 
	potVal = myPot.read_u16() #u 16 represents the amount of volts in bits so we are reading 2 ^ 16
	Voltage = (100/65106)(potVal) - (43000/65106) 
	print(potVal)
	sleep(0.5)

	if voltage < 80:
		redPin.value(0)
		yellowPin.value(0)
		green.value(1)
elif voltage >= 80 and voltage < 95:
		redPin.value(0)
		yellowPin.value(1)
		green.value(0)
elif voltage >= 95:
		redPin.value(1)
		yellowPin.value(0)
		green.value(0)

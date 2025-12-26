#Our range is 3.3V to 0V
#For our Raspberry Pi we can read analog signals in 3 different pins 31, 32, 34 so GP26 GP27 and GP28 

#Read a potentiometer in bits

import machine
from time import sleep 

potPin = 28 # the pin in which we are reading the potentiometer on GP28
myPot = machine.ADC(potPin) #the variable that reads the amount of volts off of the analog

while True: 
	potVal = myPot.read_u16() #u 16 represents the amount of volts in bits so we are reading 2 ^ 16
	print(potVal)
	sleep(0.5)

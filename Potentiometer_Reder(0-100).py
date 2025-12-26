# Homework: Use the same potentiometer but make it read between the range of 0 to 100  
# MATH:
"""Find the slope of (430,0) and (65536,100) in order to convert the bits to volts
The slope is (100)
To find the y intercept we substitute the point (430,0) and slope into y - y1 = m(x - x1)
y = (100/65106)(x) - (43000/65106) 
Voltage = (100/65106)(potVal) - (43000/65106)"""
#Read a potentiometer in volts

import machine
from time import sleep 

potPin = 28 # the 
myPot = machine.ADC(potPin) #the variable that reads the amount of volts off of the analog

while True: 
	potVal = myPot.read_u16() #u 16 represents the amount of volts in bits so we are reading 2 ^ 16
	Voltage = (100/65106)*(potVal) - (43000/65106) 
	print(potVal)
	sleep(0.5)

#Our values read from a range of -0.24 to 99.99 which can be rounded to 0 to 100

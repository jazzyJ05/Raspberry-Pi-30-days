“ “ “Find the slope of (430,0) and (65536, 33) in order to convert the bits to volts
The slope is (3.3/65106)
To find the y intercept we substitute the point (430,0) and slope into y - y1 = m(x - x1)
y = (3.3/65106)(x) - (430 * 3.3 / 65106) 
Voltage = (3.3/65106)(potVal) - (430 * 3.3 / 65106) “ “ “
#Read a potentiometer in volts

import machine
from time import sleep 

potPin = 28 # the 
myPot = machine.ADC(potPin) #the variable that reads the amount of volts off of the analog

while True: 
	potVal = myPot.read_u16() #u 16 represents the amount of volts in bits so we are reading 2 ^ 16
	Voltage = (3.3/65106)(potVal) - (430 * 3.3 / 65106) 
	print(potVal)
	sleep(0.5)

# our number range goes -0.008 to 3.29 which is close to 0 to 3.3

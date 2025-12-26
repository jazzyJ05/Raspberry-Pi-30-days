# We connect our pin wire(red) to the gp15 pin then to the long leg, then connect the short leg to a 220 resistor and connect the resistor to ground(black)

# turns on the red LED
From machine import PIN
From time import sleep 
redLED = Pin(15, Pin.OUT)
redLED.value(1)

# makes the LED blink
From machine import PIN
From time import sleep 
redLED = Pin(15, Pin.OUT)

while True:
	myLED.value(0)
	sleep(1)
	myLED.value(1)
	sleep(2)

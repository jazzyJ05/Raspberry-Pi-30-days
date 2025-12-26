#this turns the led on
From machine import PIN
myLED = Pin(‘LED’, Pin.OUT)
myLED.value(1)

#this turns the led off
From machine import PIN
myLED = Pin(‘LED’, Pin.OUT)
myLED.value(0)

#this turns the led blink
From machine import PIN
From time import sleep #allows time to be included in seconds , sleep allows the code to switch off for a given time)
myLED = Pin(‘LED’, Pin.OUT)
while True: 
myLED.value(1)
sleep(1) - stops for 1 second
myLED.value(0)
sleep(1)

#this turns the led blink
From machine import PIN
From time import sleep #allows time to be included in seconds , sleep allows the code to switch off for a given time)
myLED = Pin(‘LED’, Pin.OUT)
while True: 
myLED.toggle() #alternates the LED value between 0 and 1
sleep(.1)

#HOMEWORK
#The perimeter in which we can no longer view the led blinking more specifically the perimeter is 0.01<x<0.02 and more likely 0.01<x<0.015
From machine import PIN
From time import sleep #allows time to be included in seconds , sleep allows the code to switch off for a given time)
myLED = Pin(‘LED’, Pin.OUT)
while True: 
myLED.toggle(0.011) #alternates the LED value between 0 and 1
sleep(.1)

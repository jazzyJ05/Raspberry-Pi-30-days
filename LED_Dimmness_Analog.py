# Homework: create an LED that controls the dimness based on the voltage
#the code will be the exact same as the outpin is still releasing certain voltages as long as you keep the led connected to outpin you will be okay
from machine import PWN, Pin
from time import sleep

outPin = 16
analogOut = PWM(Pin(outPin))

analogOut.Freq(1000)
analogOut.duty_u16(0)

while True:
	myVoltage = float(input(‘What Voltage would you like’))
	pwmVal = (65550/3.3) * myVoltage
	analogOut.duty_u16(int(pwmVal))
	print(pwnVal)
	sleep(0.1)

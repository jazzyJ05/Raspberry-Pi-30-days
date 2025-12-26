# Homework: create an LED that controls the dimness based on the potentiometer
from machine import PWN, Pin
import machine
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)

outPin = 16
analogOut = PWM(Pin(outPin))

analogOut.Freq(1000)
analogOut.duty_u16(0)

while True:
	Voltage = float((3.3/65106) * (potVal) - ((430 * 3.3) / 65106))
	pwmVal = (65550/3.3) * Voltage
	analogOut.duty_u16(int(pwmVal))
	print(Voltage)
	sleep(0.1)



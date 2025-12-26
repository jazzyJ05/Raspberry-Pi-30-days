while True: 
	CMD = input(‘What Do You Want the LED to Be?’)
	print(CMD) #print the user answer in STRINGS so they will not read numbers as integers
—-----------------------------------------------------------------------------------------------------

while True:
#if we were adding two answers they will add the characters not the numbers
	CMD = input((‘What Do You Want the LED to Be?’))
	CMD2 = input((‘Something else’))
	z = CMD + CMD 2
	print(z)

—-----------------------------------------------------------------------------------------------------

while True:
#type casting, changing how the input is being read -> 
CMD = float(input(‘What Do You Want the LED to Be?’))
	CMD2 = float(input(‘Something else’))
	z = CMD + CMD 2
	print(z)
#this will print out 10.00 as floats are decimals numbers so the answer will print out a decimal

—-----------------------------------------------------------------------------------------------------

while True:
	myInput(float(input(‘Input Your Number: ’ ))

	#print out “your number is 5” if user inputs 5
	if myInput == 5:
		print (‘Your number is 5!’) 
	#print out “your number is not 5” if user inputs any number other than 5 
	if myInput != 5:
		print(‘Your number is NOT 5!’)
	#print out “your number is less than 5” if user inputs a number less than 5
if myInput < 5:
		print(‘Your number is less than 5!’)
	#print out “your number is greater than 5” if user inputs a number greater than 5
	if myInput > 5:
		print(‘Your number is greater than 5!’)

#print out “your number is less than or equal to  5” if user inputs a number less than  or equal to 5
	if myInput <=  5:
		print(‘Your number is less than or equal to 5!’)
	#print out “your number is greater than or equal 5” if user inputs a number greater than or equal to  5
	if myInput >=  5:
		print(‘Your number is NOT 5!’)


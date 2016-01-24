## Generates a list that can be used to set pixels on a SenseHat
## Can be used to be display a number from 0 to 99 on a Sensehat

X = (255,0,0) # Red
O = (0,0,0) # Off

retval = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

digits = {
	'0' : [
	    O, X, X, O, 
	    X, O, O, X,
	    X, O, O, X,
	    X, O, O, X,
	    X, O, O, X,
	    X, O, O, X,
	    X, O, O, X,
	    O, X, X, O 
	],
	'1' : [
	    O, O, X, O, 
	    O, X, X, O,
	    O, O, X, O,
	    O, O, X, O,
	    O, O, X, O,
	    O, O, X, O,
	    O, O, X, O,
	    O, O, X, O 
	],
	'2' : [
	    O, X, X, O, 
	    X, O, O, X,
	    O, O, O, X,
	    O, O, X, O,
	    O, X, O, O,
	    X, O, O, O,
	    X, O, O, O,
	    X, X, X, X 
	],
	'3' : [
	    O, X, X, O, 
	    X, O, O, X,
	    O, O, O, X,
	    O, X, X, O,
	    O, X, X, O,
	    O, O, O, X,
	    X, O, O, X,
	    O, X, X, O 
	],
	'4' : [
	    X, O, O, X, 
	    X, O, O, X,
	    X, O, O, X,
	    X, X, X, X,
	    O, O, O, X,
	    O, O, O, X,
	    O, O, O, X,
	    O, O, O, X 
	],
	'5' : [
	    X, X, X, X, 
	    X, O, O, O,
	    X, O, O, O,
	    X, X, X, O,
	    O, O, O, X,
	    O, O, O, X,
	    O, O, O, X,
	    X, X, X, O 
	],
	'6' : [
	    O, X, X, O, 
	    X, O, O, O,
	    X, O, O, O,
	    X, X, X, O,
	    X, O, O, X,
	    X, O, O, X,
	    X, O, O, X,
	    O, X, X, O 
	],
	'7' : [
	    X, X, X, X, 
	    O, O, O, X,
	    O, O, X, O,
	    O, O, X, O,
	    O, X, O, O,
	    O, X, O, O,
	    X, O, O, O,
	    X, O, O, O 
	],
	'8' : [
	    O, X, X, O, 
	    X, O, O, X,
	    X, O, O, X,
	    O, X, X, O,
	    O, X, X, O,
	    X, O, O, X,
	    X, O, O, X,
	    O, X, X, O 
	],
	'9' : [
	    O, X, X, O, 
	    X, O, O, X,
	    X, O, O, X,
	    X, O, O, X,
	    O, X, X, X,
	    O, O, O, X,
	    O, O, O, X,
	    O, O, O, X 
	]
}

def leftdigit(num):
	c=0 # row counter
	for i in enumerate(retval):
		# Only fill if on the left side of the display
		if i[0]%8 < 4:
			retval[i[0]] = digits[str(num)][c]
			c+=1
	return

def rightdigit(num):
	c=0 # row counter
	for i in enumerate(retval):
	        # Only fill if on the right side of the display 
		if i[0]%8 >= 4:
			retval[i[0]] = digits[str(num)][c]
			c+=1
	return

def blankleft():
	c=0
	for i in enumerate(retval):
		if i[0]%8 < 4:
			retval[i[0]] = O
			c+=1
	return


def makedigit(num):
	# some error handling
	if num<0: num=0
	if num>99: num=99
	# if less than 10 leave left side emtpy
	if num>9: leftdigit(num/10)
	else: blankleft()
	# do some modulus to get the last digit
	rightdigit(num%10)
	return retval



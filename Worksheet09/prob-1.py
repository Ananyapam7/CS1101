prime_numbers = 0

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

def printprime(a,b):
	for i in range(a+1,b):
		if(is_prime_number(i)):
			print i
x=input()
y=input()
printprime(x,y)
	

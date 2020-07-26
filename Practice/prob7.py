prime_numbers = 0

def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

'''def printprime(N):
	for i in range(1,N):
		if(is_prime_number(i)):
			print i'''
def goldbach(n):
	for i in range(1,n):
		for j in range(1,n):
			if(is_prime(i) and is_prime(j)):
				if (i+j)==n:
					return True
				
N=input("Enter number ")
for k in range (1,N):
	if (goldbach(k)==None):
		print k
	

n=int(input("Enter number "))
def factorial(n):
		if (n==0):
			y=1
		else:
			y=n*factorial(n-1) 
		return y
print factorial(n)

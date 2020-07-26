from math import* 
def funct(x):
	return x**(0.9)
x=10
iterations=0
while(x>2):
	x=funct(x)
	iterations=iterations+1
print iterations

import math
def mysin(x):
	s=1.
	T=1.
	n=1
	inaccuracy=abs(math.sin((math.pi)/2)-s)
	while inaccuracy>1e-4:
		T=-1*((x*x)/((2*n-1)*(2*n-2)))*T
		s=s+T
		inaccuracy=abs(math.sin((math.pi)/2)-s)
		n=n+1
	return s,n,inaccuracy
Sum,nmb,acc=mysin((math.pi)/2)
print "The number of terms computed is ",nmb
print "The actual value is ",Sum
print "The calculated value is ",math.sin((math.pi)/2)
print "The absolute difference is ",acc

import math
def myexp(x):
	s=1.
	T=1.
	n=1
	inaccuracy=abs(math.exp(math.pi)-s)
	while inaccuracy>1e-4:
		T=(x/n)*T
		s=s+T
		inaccuracy=abs(math.exp(math.pi)-s)
		n=n+1
	return s,n,inaccuracy
Sum,nmb,acc=myexp(math.pi)
print nmb,Sum,math.exp(math.pi),acc
print "The number of terms computed is ",nmb
print "The actual value is ",Sum
print "The calculated value is ",math.sin((math.pi)/2)
print "The absolut difference is ",acc

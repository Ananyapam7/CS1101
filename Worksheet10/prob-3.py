from math import*
def mylog(x):
	return log(x)/(1+log(x))
for i in range(1,21,1):
	print mylog(i*0.1)

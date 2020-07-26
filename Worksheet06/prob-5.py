x=[5,0,3,1,2,8,9,0,4,7,13,16]
y=[-7,0,-1,-3,-4,3,8,9,11,-2,10]

p=x[0]
for j in range (0,len(x)):
	
	if p<x[j]:
		p=x[j]
print p

q=y[0]
for i in range (0,len(y)):
	
	if q<y[i]:
		q=y[i]
print q


	

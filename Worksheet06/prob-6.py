x=[5,0,3,1,2,8,9,0,4,7,13,16]
y=[-7,0,-1,-3,-4,3,8,9,11,-2,10]

p=x[0]
q=x[0]
w=0
z=0
for i in range (0,len(x)):
	
	if p<x[i]:
		p=x[i]
		z=i
	if q>x[i]:
		q=x[i]
		w=i
print "max",p,"pos",z+1,"\nmin",q,"pos",w+1

r=y[0]
s=y[0]
b=0
a=0
for i in range (0,len(y)):
	
	if r<y[i]:
		r=y[i]
		a=i
	if s>y[i]:
		s=y[i]
		b=i
print "max",r,"pos",a+1,"\nmin",s,"pos",b+1





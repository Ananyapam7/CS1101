def isperfect(n):
	s=0
        
	for i in range(1,int(n//2)+1):
		if(n%i==0):
			s=s+i
	if(s==n):
		return n

#for k in range(1,1000):
j=0
k=1
while(j<4):
      m=isperfect(k)
      if(m!= None):
	print m
        j+=1
      k+=1

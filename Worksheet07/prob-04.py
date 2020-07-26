n = int(input("n = "))
i=1
lst=[]
while(i<=n):
	lst.append(sum(k**2 for k in range (1,i+1)))
	i+=1
print lst

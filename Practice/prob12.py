def sum_of_multiples(N):#returns sum of multiples of 3 or 5 below N
	s=0	
	for i in range(N):
		if(i%3==0 or i%5==0):
			s=s+i
	return s
print sum_of_multiples(100)

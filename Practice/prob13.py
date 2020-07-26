#Fibonacci sequence up to n-th term using recursive functions

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms=1
s=0
while recur_fibo(nterms)<100:
	if(recur_fibo(nterms)%2==0):
		s=s+recur_fibo(nterms)
		nterms+=1
	else:
		nterms+=1
print s


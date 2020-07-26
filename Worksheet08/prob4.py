def series(n):
	return sum([i/(i+1.0) for i in range (1, n+1)])
for n in range (1,21):
	print (n, series(n))


n= input(" n :")
p=[]
for i in range(n):
  j="input element " + str(i+1) + ":"
  b=input(j)
  p.append(b)
a=max(p)
b=min(p)
for k in range(n):
  if (a==p[k]):
	print "Maximum is ",a,"in position ",k+1 
for l in range(n):
  if (b==p[l]):
	print "Minimum is ",b,"in position ",l+1     

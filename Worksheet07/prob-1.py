
n = int(input("n = "))

# Initialize a variable for keeping the total
squaretotal = 0
cubetotal = 0

# Next loop iterates over all integers from 1 to N
# At each stage, the current integer square is added to total
for i in range(1,n+1):
    squaretotal += i*i
    cubetotal +=i*i*i

# Print the calculated total
print "The caluclated  square total is", squaretotal
print "The caluclated  cube total is", cubetotal

# Print known value of total 
print "The expected square total is", n*(n+1)*(2*n+1)/6
print "The expected cube total is", n*(n+1)*n*(n+1)/4



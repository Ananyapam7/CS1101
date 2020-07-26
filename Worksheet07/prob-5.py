n = int(input("n = "))

# Initialize a variable for keeping the total
total = 2.0

# Next loop iterates over all integers from 1 to N
# At each stage, the current integer square is added to total
for i in range(1,n+1):
    total=1+ i/(total)


# Print value of total 
print "The  total is",total

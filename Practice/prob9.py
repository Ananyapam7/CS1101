'''count=0
def countaplha(x,ch):
	for key in x:
		if(key==ch):
			count=count+1
	return count

name=input("Enter a string ")
print countalpha(name,a)'''



string = input("Enter a string ")
ch=input("Enter a charecter ")
def countvar(string, var):
    found = 0
    for key in string:
        if key == var:
            found += 1
    return found
countvar(string, var)
print 'count of %s is: %s ' %(var, countvar(string, var))



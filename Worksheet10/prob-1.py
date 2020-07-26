
x=int(input())
y=int(input())
z=int(input())
def is_triangular(x,y,z):
    if(x+y>z and z+y>x and x+z>y):
	return True
    else:
	return False
print is_triangular(x,y,z)

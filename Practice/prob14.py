import math
N=600851475143
def prime_factors(n):
    num = []

    #add 2 to list or prime factors and remove all even numbers(like sieve of ertosthenes)
    while(n%2 == 0):
        num.append(2)
        n /= 2

    #divide by odd numbers and remove all of their multiples increment by 2 if no perfectlly devides add it
    for i in xrange(3, int(math.sqrt(n))+1, 2):
        while (n%i == 0):
            num.append(i)
            n /= i

    #if no is > 2 i.e no is a prime number that is only divisible by itself add it
    if n>2:
        num.append(n)

    print (num)
prime_factors(N)

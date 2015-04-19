def gcd(a, b):

	  if b == 0:
        return a

    return gcd(b, a % b)
"""
	a, b = b, a%b
	if b != 0:
		gcd(a,b)
	return a
		

    while b:
        a, b = b, a%b
    return a


def gcd(a,b):
	
	c = a/b
	d = a%b
	
	if d > 1 and c != 1:
		a = b
		b = d
		#print(a,b,c,d)

		gcd(a,b)
	else:
		b = 1	
	return b	
"""


a = input()
b = input()
a, b = max(a,b), min(a,b)
print(gcd(a,b))
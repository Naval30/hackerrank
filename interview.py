
def inbetween(str1, str2):

	c = -1
	d = 0
	for char in str2:
		print str1.index(char)
		print c
		if char in str1: # and c < str1.index(char):
			print char
			c = str1.index(char)
			d += 1
		
	if d == len(str2):
			return True
	else:
			return False		





str1 = raw_input()
str2 = raw_input()

print inbetween(str1, str2)

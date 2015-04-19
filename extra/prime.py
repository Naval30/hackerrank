def prime(x):

	y = 2
	z = x/2

	while y < z:
		if (y%2 == 0):
			y += 1
		else:
			if (x%y == 0):
				print y
				largest = y
			y +=1



prime(54)


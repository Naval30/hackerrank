def fibonacci(item):
	if item == 1:
		ans = 0
	elif item == 2:
		ans = 1
	else:
		ans = fibonacci(item-1) +fibonacci(item-2)	
	return ans	


print fibonacci(6)

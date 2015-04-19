def insertionSort(alist):
	for i in range(1,len(alist)):
		num = alist[i]
		position = i

		while(num < alist[i-1] and i > 0):
			alist[i] = alist[i-1] 
			i -=1
		alist[i] = num 
	return alist	
		

			




m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)
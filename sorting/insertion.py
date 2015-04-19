def insertionSort(ar):  
	
	var =ar[-1]  
	found = False
	for i in range(-1, -len(ar)-1, -1):
		if i == -len(ar) and found == False:
			ar[0] = var
			found = True
			print " ".join(map(str, ar))

		if(found == False):
			ar[i] = ar[i-1]
			if(ar[i-1] < var):
				ar[i] = var
				found = True
			print " ".join(map(str, ar))	


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
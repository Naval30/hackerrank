def twostrings(input1, input2):
	#input1.lower()
	#input2.lower()

	if len(input1) < len(input2):
		for char in input1:
			if char in input2:
				return 1
	else:
		for char in input2:
			if char in input1:
				return 1
				
	return 0		 





input_f = int(raw_input())

for i in range(input_f):
	input1 = raw_input()
	input2 = raw_input()
	if twostrings(input1, input2) == 1:
		print "YES"
	else:
		print "NO"	



def strrev(str1):
	if len(str1) == 1:
		return str1
	else:
		strrev = str1[:-1] + str(strrev(str1[:-1]))
	return strrev	 


str1 = raw_input()
print strrev(str1)





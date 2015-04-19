def unqi(cstr):
	
	char_set = []
	for i in range(256):
		char_set.append(False)
	for char in cstr:
		if char_set[ord(char)] == True	:
			return False
		else	:
			char_set[ord(char)] = True	
	return True

str1 ="jasdassdkh  "


if unqi(str1):
	print("True")
else:
	print("False")	

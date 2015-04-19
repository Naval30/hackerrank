def panagram(sen):
	sen = sen.lower()
	string = "abcdefghijklmnopqrstuvwxyz"
	for char in string:
		if char not in sen:
			return False
	return True		

	"""
	sen = sen.lower()
	dic = {}
	for key in range(97,123):
		dic[key] = False

	for char in sen:
		if ord(char) in dic:
			dic[ord(char)] = True
	
	var =True

	for index in range(97,123):
		if dic[index] == False:
			var = False

	return var		

"""
sen = raw_input()
print panagram(sen)
"""
ans = panagram(sen)

if ans == True:
	print "panagram"
else:
	print "not panagram"
	"""
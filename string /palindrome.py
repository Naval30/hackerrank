def palindrome(strinp):
	var = False
	var1 = 0
	var2 = 0
	for index in range(len(strinp)/2):
		if strinp[index] == strinp[-(index+1)] and index != -(index+1):
			var = True
		else:
			var1 = index
			var2 = -(index+1)
			var2 = len(strinp) + var2 
			return (False, var1, var2)
	return var		

def checkpalindrome(strinp):
	var = 0
	ans = palindrome(strinp)
	if ans == True:
		var = -1
	else:
		var0, var1, var2 = ans
		if var1 == 0 :
			strinp1 = strinp[:-1]
			strinp = strinp[1:]
		else:	
			strinp1 = strinp[:var2]+strinp[var2+1:]
			strinp = strinp[:var1]+strinp[var1+1:]
			
		ans1 = palindrome(strinp)
		ans2 = palindrome(strinp1)

		if ans1 == True:
			var = var1
		else:
			var = var2	 

	return var	

"""
t = int(raw_input())
for _ in xrange(t):
	print checkpalindrome(raw_input())
"""
m = int(raw_input())

list1 = []
for i in range(0,m):
    a = raw_input()
    list1.append(a)


for char in list1:
    res = checkpalindrome(char)
    print res

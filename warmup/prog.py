#!/usr/bin/py
def lonelyinteger(a,b):
	dic = {}
	for char in b:
		if char not in dic:
			dic[char] = False
		else: 
			dic[char] = True	

	for char in dic:
		if dic[char] == False:
			return char		

			
"""
	var = 0

	for char in dic:
		if dic[char] == False:
			var +=1		
	
	if var == 1:
		return True
	else:
		return False		
"""
   
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(a, b)

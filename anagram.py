from collections import Counter

def anagram(word1,word2):
	var = False
	if len(word1) != len(word2):
		return False
	else:
		list1 = list(word1)
		list2 = list(word2)
		list1.sort()
		list2.sort()
		if list1 == list2:
			return True
		else:
			return False	
	

def checkword(word1, word2):
	list1 = list(word1)
	list2 = list(word2)
	a = Counter(list1) - Counter(list2)
	sum = 0

	for i,j in a.items():
		sum = sum+j

	return sum



def check(word):
	var = 0
	leng = len(word)
	if leng%2 != 0:
		var = -1
		return var

	word1 = word[:leng/2]
	word2 = word[leng/2:]	

	if anagram(word1, word2) == True:
		var = 0
		return var

	else :
		var = checkword(word1, word2)
		return var


m = int(raw_input())

list1 = []
for i in range(0,m):
    a = raw_input()
    list1.append(a)

for char in list1:
    res = check(char)
    print res



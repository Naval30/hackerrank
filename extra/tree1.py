def binary(r):
	return [r,[], []]

def insertleft(root, left):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [left, t, []])
	else:
		root.insert(1, [left, [], []])
	return root		

def insertright(root, right):
	t = root.pop(2)
	if (len(t) > 1):
		root.insert(2, [right, [], t])
	else:
		root.insert(2, [right, [], []])
	return root
	
def getrootval(root):
	return root[0]

def setrootval(root, new):
	root[0] == new

def getleftchild(root):
	return root[1]

def getrightchild(root):
	return root[2]

r = binary(3)
insertleft(r,4)
insertleft(r,6)
insertright(r,5)
insertright(r,7)
print(getleftchild(r))
print(setrootval(r,4))
print(getrightchild(r))	
print(getrightchild(getrightchild(r)))	
print(getrightchild(r))
print(getlefttchild(r))
#class Node:

class Node:
	def __init__(self, parent, left, right):
		self.left = left
		self.right = right
		self.parent = parent



class BinaryTree:
	def __init__(self):
		self.root = 1


	def add(self, input1, i):	
		if i == 0:
			if (input1[0] == -1):
				input1[0] = None
			if (input1[1] == -1):
				input1[1] = None
	
			current = Node(self.root, input1[0], input1[1])






input1 = int(raw_input())
tree = BinaryTree()
list1 = []
list2 = []

for i in range(input1):
	input2 = map(int, raw_input().split())
	list1.append(input2)

input3 = int(raw_input())
for i in range(input3):
	input4 = int(raw_input())
	list2.append(input4)


for i in range(input1):
	tree.add(input1[i], i)	

"""
print list1	

for i in range(input1):
	tree.add(input1, i)	

 """

i = 0 => 1
	1 => 2
	2 => 2
	3-6 => 3
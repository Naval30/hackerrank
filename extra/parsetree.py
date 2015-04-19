#from pythonds.basic.stack import Stack
#from pythonds.trees.binaryTree import BinaryTree

class Stack:

    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, data):
        self.items.insert(0, data)  

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def parsetrees(item):
        item1 = item.split()
        stackp = Stack()
        etree = BinaryTree('')
        stackp.push(etree)
        current = etree
        for i in item1:
            if i == '(':
                current.insertLeft('')
                stackp.push(current)
                current = current.getLeftChild()
            elif i in ['+', '-', '/', '*']:
                current.setRootVal(i)
                current.insertRight('')
                stackp.push(current)
                current = current.getRightChild()
            elif i not in ['+', '-', '*', '/', '(', ')']:
                current.setRootVal(int(i))
                parent = stackp.pop()
                current = parent   
            elif i == ')' 
                parent = current.pop()
                current = parent 
            else
                raise ValueError:
            -    --+

        return etree               


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#pt.postorder()  #defined and explained in the next section
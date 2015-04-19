def utopian(a, c):
    list1 = []
    for char in c:
    	height = 1
    	#print char
        for l in range(1, char+1):
            if (l%2 == 0):
                height = height+1
            elif (l%2 == 1):
                height = 2*height
         #   print height   

        list1.append(height) 
    return list1    


a = int(input())
c = []
for i in range(0,a):
    b = int(input())
    c.append(b)
    
list2 = utopian(a,c)
for p in list2: 
    	print p   



"""
def solveMeSecond(a,b):
   return a+b
n = int(input())
for i in range(0,n):
    a, b = input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print (res)


    """
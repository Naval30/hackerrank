# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())

def multisum(k, C):
    D = [False for _ in range(k+1)]
    D[0] = True
    print D
    for i in range(1,k+1):
        D[i] = any([D[i-c] for c in C if i - c >= 0])
    print D    
    for i in reversed(range(k+1)):
        if D[i]:
            return i
    return None

for i in range(T):
    n, k = map(int, raw_input().strip().split(' '))
    C = map(int, raw_input().strip().split(' '))
    print multisum(k,C)






for i=1
d[1] = any(D[1],D[0]) 
d[2] = any(d[1],d[2],d[0])










"""

testcase = raw_input()

for i in testcase:
	"""
sumw = int(raw_input())
n = map(int, raw_input().split(" "))
	
print knapsack(sumw,n)	
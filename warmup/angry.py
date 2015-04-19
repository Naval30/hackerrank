
def angry(c,list1):
    lowest = list1[-1] - list1[0]
    for i in range(0,len(list1)-c+1):
        lowest = min(lowest, list1[i + c - 1] - list1[i])
      
    return lowest       

n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = angry(k, candies)

print min_diff

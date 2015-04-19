def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     print " ".join(map(str, alist))  
   

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
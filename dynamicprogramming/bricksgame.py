
t = int(raw_input())
for i in range(t):

    n = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    
    ######
    def calc(arr):
        alen = len(arr)
        if alen < 4:
            return sum(arr)
        '''
        Both DP[] and PreSum[] is in terms of bottom-up
        because opponent 'your friend will also play optimally'
        '''
        #    Calc prefix sum
        presum = [0] * alen
        presum[0] = arr[0]
        for i in range(1, alen):
            presum[i] = presum[i - 1] + arr[i]
        print presum    
            
        #    Go DP
        dp = [0] * (alen)        
        dp[0] = arr[0]
        dp[1] = arr[1] + dp[0]
        dp[2] = arr[2] + dp[1]
        for i in range(3, alen):
            # Take 1: (i), opponent will take dp[i - 1]
            x = arr[i] + presum[i - 1] - dp[i - 1]
            # Take 2
            y = presum[i - 2] + arr[i] + arr[i - 1] - dp[i - 2]
            # Take 3
            z = presum[i - 3] + arr[i] + arr[i - 1] + arr[i - 2] - dp[i - 3]
            print x,y,z

            dp[i] = max(x, y, z)
            print dp[i]
            
        return dp[alen - 1]
    ######    
    # reverse to bottom -> top
    arr.reverse()
    print (calc(arr))

"""
def brick(input2):
	for i in range(len(input2)):
		sum1 = sum(input2[i], input2[i+4:i+7])
		sum2 = sum(input2[i:i+2], input2[i+5:i+8])
		sum3 = sum(input2[i:i+3], input2[i+6:i+9])

		if max(sum1, sum2, sum3) == sum3:
			var1 = sum(input_2[i:i+3])
		elif max(sum1, sum2, sum3) == sum2:	
			var1 = sum(input_2[i:i+2])
		elif max(sum1, sum2, sum3) == sum1:	
			var1 = sum(input_2[i:i+1])	


input1 = raw_input()
input2 = map(int, raw_input().split())
print input2	

#input1 = int(raw_input())
5

sum(i,i+1,i+2) > sum(i+3, i+4, i+5):

sum(i:i+3) > sum(i+3:i+6)



10 3
	

1, 5, 6, 7
1, 2, 6, 7, 8
1, 2, 3, 7, 8, 9

max(sum(input2[i], input2[i+4:i+7]), 
	sum(input2[i:i+2], input2[i+5:i+8])
	sum(input2[i:i+3], input2[i+6:i+9])
	)

10 9 8 3 45 5 19 7 23 45

10 9 8
3
4 5
19 7 23
45

10 9 8
3
4 5 19
7 23 45

6

1 2 3 4 5 6

4 3 2 7 8 3 4 10

i = 0
1 if sum of(1,2) > 3,4,5 

4
12

4 5 10 7 8 3 4 10

51

33, 18
3
3
2



4
5 10 7

432

783

4 10

1, if sum(of next 2) <  
i
1 if i+3 is big
2 if  

4

3 2 7

8 3 4

10
"""
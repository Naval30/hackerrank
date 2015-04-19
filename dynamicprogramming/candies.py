def candies(input_2):

	list2 = [1] * len(input_2)


	for i in range(1, len(input_2)):
		if input_2[i] > input_2[i-1]:
			list2[i] = list2[i-1] + 1


	for i in range(len(input_2)-2, -1, -1):		
		if input_2[i] > input_2[i+1]:
			list2[i] = max(list2[i], list2[i+1] + 1)

	return list2, sum(list2)


input1 = int(raw_input())

input_2 = [int(raw_input()) for i in range(input1)]

print candies(input_2)

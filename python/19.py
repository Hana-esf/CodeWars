#solve this using dynamic programming
#Kadane's Algorithm
def max_sequence(arr):
    print(sum(arr))
    if len(arr) == 0:
        return 0
 
    #check if all the elements in the list are negative, return 0
    if (any(i>0 for i in arr)) == False:
        return 0

    total_sum = arr[0]
    current_max = 0

    for i in range(len(arr)):
        current_max += arr[i]

        if current_max < 0:
            current_max = 0

        elif total_sum < current_max:
            total_sum = current_max
    return total_sum


#main
input_list = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
print(max_sequence(input_list))
	


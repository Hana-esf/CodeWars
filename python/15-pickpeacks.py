def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    i = 1
    print(arr)
    while i < len(arr)-1:
        if arr[i] > arr[i-1]:
                count = 0
                while i < len(arr)-1 and arr[i] == arr[i+1]:
                    count += 1
                    i += 1
                if i == len(arr)-1:
                    break
                if arr[i] > arr[i+1]:
                    if arr[i] == arr[i-1]:
                        result['pos'].append(i-count)
                    else:
                        result['pos'].append(i)
                    result['peaks'].append(arr[i])
                    i += 1
        i += 1
    return result


#main
#input_arr = [int(i) for i in input('Enter the list : ').split()]
input_arr = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]
print(pick_peaks(input_arr))
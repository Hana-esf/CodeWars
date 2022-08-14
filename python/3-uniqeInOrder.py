# def unique_in_order(iterable):
#     unique_list = []
#     if len(iterable) == 1:
#         unique_list.append(iterable)
#         return unique_list
    
#     i = 0
#     while i < (len(iterable)):
#         unique_list.append(iterable[i])
#         if i == len(iterable)-1:
#             break
#         while iterable[i] == iterable[i+1]:
#             i = i + 1
#             if i == len(iterable)-1:
#                 break
#         i = i + 1
#     return unique_list

def unique_in_order(iterable):
    unique_list = []
    for i in iterable:
        if unique_list == []:
            unique_list.append(i)
        else:
            if unique_list[-1] != i:
                unique_list.append(i)
    return unique_list


#main
#iterable = "AAAABBBCCDAABBB"
iterable_var = input('Enter the iterable : ')
print(unique_in_order(iterable_var))

# from collections import Counter
# def first_non_repeating_letter(str):
#     result_str = ''
#     freq = Counter(str.lower())
#     print(freq)
#     for i in freq:
#         if freq[i] == 1:
#             ind = str.find(i)
#             if ind != -1:
#                 result_str += i
#                 return result_str
#             else:
#                 result_str += i.upper()
#                 return result_str
        
#     return result_str
    
def first_non_repeating_letter(str):
    lower_str = str.lower()
    for i in str:
        if lower_str.count(i.lower()) == 1:
            return i
    return ''

#main
input_str = input("Enter the string : ")
print(first_non_repeating_letter(input_str))
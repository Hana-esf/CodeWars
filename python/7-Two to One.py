# from collections import OrderedDict
# def longest(a1, a2):
#     distinct_str = "".join(OrderedDict.fromkeys(a1)) + "".join(OrderedDict.fromkeys(a2))
#     sorted_list = sorted(distinct_str)
#     sorted_str = ""
#     distinct_str = "".join(OrderedDict.fromkeys(sorted_str.join(sorted_list)))
#     return distinct_str
def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))

#main
s1 = input('Enter first string : ')
s2 = input('Enter second string : ')
print(longest(s1,s2))
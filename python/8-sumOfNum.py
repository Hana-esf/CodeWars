# def get_sum(a,b):
#     if a == b:
#         return a
    
#     if b < a:
#         a, b = b, a
#     total_sum = 0
#     for i in range(a,b+1):
#         print(i)
#         total_sum = total_sum + i
#     return total_sum
def get_sum(a,b):
    return sum([x for x in range(min(a,b),max(a,b)+1)])

#main

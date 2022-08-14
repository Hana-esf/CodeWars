def solution(number):
    sum = 0
    for i in range(1,number):
        if i%3 == 0 or i%5 == 0:
            sum = sum + i
    return sum

#main
# num = int(input('Enter the number : '))
# print(solution(num))
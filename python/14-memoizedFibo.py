fib_dic = {0 : 0 , 1 : 1}
def fibonacci(n):
    if n in [0, 1]:
        fib_dic[n]
        return n
    if n not in fib_dic:
        f1 = fibonacci(n - 1) 
        f2 = fibonacci(n - 2)
        fib_dic[n] = f1 + f2
    return fib_dic[n]

    
#main
fib_n = int(input('Enter the n : '))
print(fibonacci(fib_n))
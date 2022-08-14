def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
    

S = input('Enter XO string : ')
print(xo(S))
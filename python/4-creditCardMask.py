def maskify(cc):
    if len(cc) < 4:
        return cc
    
    maskedstr = ""
    for i in cc[:-4]:
        maskedstr = maskedstr + '#'

    for i in cc[-4:]:
        maskedstr = maskedstr + i
    
    return maskedstr


#main
# credit_str = input('Enter the pass : ')
# print(type(credit_str))
# print(maskify(credit_str))


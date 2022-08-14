def rot13(message):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETS = alphabets.upper()
    Rot13_str = ""
    for i in message:
        if i in ALPHABETS:
            alpha = ALPHABETS
        elif i in alphabets:
            alpha = alphabets
        if i in alpha:
            if alpha.index(i)+13 > len(alpha):
                alpha_ind = 13 - (26 - alpha.index(i))
                print(alpha.index(i))
                print(i , 'in if : ',alpha_ind)
                Rot13_str += alpha[alpha_ind]
            else:
                alpha_ind = alpha.index(i)+13
                print(i, 'in else : ',alpha_ind)
                Rot13_str += alpha[alpha_ind]
        else:
            Rot13_str += i
    return Rot13_str


#main
input_str = input('Enter the string : ')
print(rot13(input_str))
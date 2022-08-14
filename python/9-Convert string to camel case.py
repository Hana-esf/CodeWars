import re
def to_camel_case(text):
    split_text = re.split(r'-|_', text)
    capt_text = split_text[0]
    for i in range(1,len(split_text)):
        cap_word = split_text[i].capitalize()
        capt_text = capt_text + cap_word
    return capt_text

    
    

#main
str_inp = input("Enter the string : ")
print(to_camel_case(str_inp))
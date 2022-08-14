def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140 : return False
    return '#' + s.title().replace(" ","")

#main
input_str = input('Enter the string : ')
print(generate_hashtag(input_str))
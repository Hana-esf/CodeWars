def recoverSecret(triplets):
    secret_chars = list(set(i for j in triplets for i in j))
    #print(secret_chars)
    secret_chars_pos = {}
    for i in triplets:
        change_place(secret_chars, i[0], i[1])
        change_place(secret_chars, i[1], i[2])
        change_place(secret_chars, i[0], i[2])
    # print('After changes:')
    # print(secret_chars)
    secret_str = ""
    secret_str = secret_str.join(secret_chars)
    #print(secret_str)

def change_place(list1, char1, char2):
    if list1.index(char1) > list1.index(char2):
        list1.remove(char1)
        list1.insert(list1.index(char2),char1)
    

#main
the_input = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
recoverSecret(the_input)
#print(recoverSecret(the_input))
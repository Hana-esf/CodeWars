import re
def recoverSecret(triplets):
    secret_chars = list(set(i for j in triplets for i in j))
    secret_chars_pos = {}
    secret_str = ""
    for i in triplets:
        temp_str = ""
        temp_str += temp_str.join(i)
        secret_str += temp_str
    
    for i in secret_chars:
        secret_chars_pos[i] = [((i.start())%3) for i in re.finditer(i,secret_str)]
    print(secret_chars_pos)
  






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
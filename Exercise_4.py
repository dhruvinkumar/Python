import random
import string
coding = int(input("Enter 1 for encode 0 for decode "))
code = input("Enter your data ")


if (coding):
    if (len(code) > 3):
        N = 3
        code = code[1:]+code[0]
        code = ''.join(random.choices(string.ascii_letters, k=N)) + code

    else:
        code = code[::-1]

    print(code)

else:

    if(len(code)>3):
       s = code[-1]
       code = code[3:len(code)-1]
       reversed(code)
       code = s + code
        
    else:
        code = code[::-1]
        
    print(code)
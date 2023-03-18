import random
import string
code = input("Enter your data ")

if(len(code)>3):
    N=3
    s = code[0]
    code = code[1:]+s
    code =  ''.join(random.choices(string.ascii_letters, k=N)) + code
    
else:
    code = code[::-1]
    
print(code)
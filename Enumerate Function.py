"""
The enumerate function is a built -in function in python
that allows you to loop over a sequence (such as list,tuple, or string)
and get the index and value of each element in the sequence at
the same time.Here's basic example of how it works:
"""
marks =  [12, 56, 32, 98, 12, 45, 1, 4]


for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index == 3):
        print("Hello, awesome!")

######################################################

s  = "string"

for i, j in enumerate(s):
    print(i,j)
    
########################################################

fruits = ["apple", "banana", "cherry"]

for i, j in enumerate(fruits):
    print(i,j)
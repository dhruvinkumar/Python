'''
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are unchangeable meaning they can not  alter after creation. (immutable)
'''
tup = (1, 2, 76, 342, 32)
# tup[0] = 20 # this will give error because tuple can't be changed
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(type(tup),tup)

if 342 in tup:
    print("Yes")

tup2 = tup[1:4]
print(tup[-3:-1])
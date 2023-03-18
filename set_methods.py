s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7}

# print(len(s1))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))

# s1.update(s2) #this will update s1 and it'll add values of s2 into s1
# s1.intersection_update(s2)

# print(s1.symmetric_difference(s2))
# print(s1.isdisjoint(s2))


s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {5, 6, 7}

# print(s1.issuperset(s2))
# print(s2.issubset(s1))

# s1.add(10)
# s1.discard(10)
# s1.remove(10) #this will raise error if element is not present 

# num = s1.pop() #pop the random item from the set
# print(num)

# s1.clear() #clear data inside s1
# del s1 #delete s1
# print(s1)

if (1 in s1):
    print("Yes")
else:
    print("No")
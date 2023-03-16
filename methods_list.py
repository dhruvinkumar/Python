l = [11, 45, 1, 2, 3, 4, 6, 1, 1, 23, 4, 55]

# l.append(7)
# l.sort(reverse=True)
# l.sort()
# print(l.index(4)) # it will return first index of occurance of that value
# print(l.count(1))

# m = l 
# m[0] = 10 # if make change in m it also do changes in l also because we have taken referance of that

# m = l.copy() # here we are taking copy of l so if we make changes in m it won't refelect in l
# m[0] = 10 # l[0] is  still 11

# l.insert(1, 899)  # list.insert(index, value)

m = [900, 200, 1000]
# l.extend(m)

k = l + m
print(k) 


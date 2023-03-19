# for immutable data structure python returns same memory 
#  location to avoid wastage of memory as they will not change
  
a = (3)
b = (3)

print(a is b) # exact location of object in memory
print(a == b) # value
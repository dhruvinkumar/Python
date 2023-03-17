'''
sets are unordered collection of data items. They stor multiple items in a single variable. Set are unchangeable  means once you construct it ,it can't be modify further.
'''
s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
    print(value)
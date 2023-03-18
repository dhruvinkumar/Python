dict = {
    "DJ": "Human being",
    "Spoon": "Object"
}
print(dict)
print(type(dict))
print(dict["DJ"])
print(dict["Spoon"])

dict = {
    114: "DJ",
    139: "Ujju",
    567: "Neha"
}
print(dict)
print(type(dict))
print(dict[139])
print(dict[114])
# print(dict["name2"]) #this will throw error
print(dict.get("name2")) #this will create none
print(dict.keys())
print(dict.items())
print(dict.values())

for i in dict:
    print(f"The value corresponding to key {i} is {dict[i]}.")


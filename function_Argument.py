# def average(a=4, b=1):
#     print("The average is", (a+b)/2)
    
# average(4,6)
# average(1,5) # this is defalut 
# average(b=9, a=5) # this is specific
# average(1)
# average(b=9)

# If we don't have any default argument than it is requierd argument.

# def name(fname, mname = "John", lname = "Whatson"):
#     print("Hello,",fname,mname,lname)

# name("Tanu","Manish","Jain")

def average(*number):   #Argument as tuple
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    return sum/ len(number)

c = average(40,50,60)
print(c)

# def name(**name):  #Argument as dictionary
#     print(type(name))
#     print("Hello,",name["fname"],name["mname"],name["lname"])
    
# name(lname = "Bhatt", mname = "DJ", fname= "Kunjal")
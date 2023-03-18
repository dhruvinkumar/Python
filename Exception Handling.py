"""
Exception handling is the process of responding to 
unwanted or unexpected events when a computer program runs.
Exception handling deals with these events to avoid the program
or system to avoid the program or system crashing, ans without 
this process, exception would distupt the normal operaton of
a program.
"""


a = input("Enter the number: ")
print(f"Multiplicaion table of {a} is:")

# ######################## Method - 1 ######################
try:
    for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")
    
print("Some lines of code")
print("end of program")

# ########################## Method - 2 #####################
try:
    for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    
print("Some lines of code")
print("end of program")

###########################################################
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
    print("Index error")
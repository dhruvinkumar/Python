for i in range(9):
    print(i+1)
else:
    print("You are out of range")
##################################################
for i in range(6):
    print(i)
    if i == 4:
        break

else :                  # this will not be printed as we are breaking the loop it will execute only when loop is successsfully completed
    print("Sorry no i")
    
#####################################################################################  
count = 5
while (count > 0):
    print(count)
    count-=1
else:              # With while loop we can use else also if it does not go inside then it will go into else block
    print("number is 0 now!!!")

#################################################################

for x in range(5):
    print(f"iteration no {x+1} in for loop")
else:
    print("else block in the loop")
print("Out of loop")
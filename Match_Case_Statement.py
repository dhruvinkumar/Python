x = int(input("Enter the value of x: "))
# x is a variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if -condition
    case 4:
        print("case is 4")
        
    # so it is basically just an else:
    case _:
        print(x)
        
# We not need to break case statement unlike C++,Java

name = 'harry' # global var

def func():
    # global  name   # TO use global var
    name = 'DJ'
    y  = 5      # local variable
    print(name)

func()
print(name)
# print(y) # We can't access local variable out of it's scope

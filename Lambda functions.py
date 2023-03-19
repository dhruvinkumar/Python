'''
In python, a lambda function is a small anonymous function
without a name.It is a defined using the lambda keyword. 
'''

# NORMALLY WRITTING OF FUNCTION

# def double(x):
#     return x*2

# LAMBDA WRITTING OF FUNCTION

double = lambda x: x*2
cube =  lambda x: x*x*x 
avg2 = lambda x, y: (x + y) / 2 
avg3 = lambda x, y, z: (x + y + z) / 3 

# print(double(2))
# print(cube(2))
# print(avg2(10,20))
# print(avg3(10,20,15))


def appl(fx,value):
    return 6 + fx(value)

print(appl(lambda x: x*x,20))
print(appl(cube,20))

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(5))

def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    
    return fib(n-1)+fib(n-2)

print(fib(0))
print(fib(1))
# print(fib(10))
print(fib(3))
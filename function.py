# Function can be user define and built-in

def gmean(a,b):
    return (a*b)/(a+b)


    
def min(a,b):
    pass       # It'll pass the function for that time
 
a = 9
b = 8
c = 8
d = 7
print(gmean(a,b))
print(gmean(c,d))
print(max(a,b))
print(max(c,d))



def max(a,b):
    if(a>b):
        return a
    else:
        return b
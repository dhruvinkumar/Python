'''
In python the map, filter and reduce functions are built-in functions
that allow you to apply a function to a sequence of element and return
a new sequence of elements and return a new sequence. These functions 
are known as higher-order functions, as they take other functions as
argument.
'''

'''
# MAP :- The map function applies a function to each element in a
         sequence containing the transformed elements. The map function
         has the following syntax:
         
         map(function , iterable)

'''

def cube(x):
    return x*x*x

# print(cube(2))

l = [1, 2, 4, 6, 5, 3]
newl = []

for i in l:
    newl.append(cube(i))


#  after map:-

newl = list(map(cube , l))
print(newl)
newl = list(map(lambda x: x*x , l))
print(newl)


'''
# FILTER :- The filter function filters a sequence of elements based
            on a given predicate (a function that returns a boolean value)
            and return a new sequeence containing only element that meet 
            predict . The filter has following syntax: 
            
            filter(predicate , iterable)
'''
def filter_function(a):
    return a>2
newnewl = list(filter(filter_function,l))
print(newnewl)
newnewl = list(filter(lambda x: x>4,l))
print(newnewl)

''''
# REDUCE :- The reduce function is a higher-order 
            function that applies a function to a
            sequence and return a single value. It 
            is a part of the functools module in
            python and has the following syntax:
            
            reduce(function, iterable)
'''

from functools import reduce 

numbers  = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y: x / y, numbers)
sum = reduce(lambda x,y: x * y, numbers)

print(sum)
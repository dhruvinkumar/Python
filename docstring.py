# python docstrings are the string literals that appear right after the defination of a function, method, class, or module.
#Comment are decscription that help programmers better undersatnd the intent and funtionality of the program. They are completely ignored by the python interpreter.
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
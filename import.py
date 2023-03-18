'''
Importing pandas is the process of loading code
from python modulre into the current script, as This 
allows you to use the functions and variables defined in 
the module in your current script, as well as any additional
modules that the imported module may depend on.
'''
import math # importing math module
import math as m # importing module with alias name
from math import sqrt,pi # importing partiular function
from math import * # importing all modules from math
from math import sqrt as s # give another name (Alias)


result = math.sqrt(4)
print(result)

result = m.sqrt(4)
print(result)

result = sqrt(9)
print(result)

result = s(16)
print(result)

import math
print(dir(math)) # it will give the list of all function in this module
print(math.sqrt, type(math.sqrt))

import DJ_MODULE as dj

dj.welcome()
print(dj.var)
print(dir(dj))

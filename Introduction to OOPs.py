'''
There are two approaches that are used to erite program or code.
1) Procedural Programming
2) Object-Oriented Programming

The procedure we are following till now is the “Procedural Programming” approach. So, in this
session, we will learn about Object Oriented Programming (OOP). The basic idea of object-oriented
programming (OOP) in Python is to use classes and objects to represent real-world concepts and
entities.

A class is a blueprint or template for creating objects. It defines the properties and methods that an
object of that class will have. Properties are the data or state of an object, and methods are the
actions or behaviors that an object can perform.

An object is an instance of a class, and it contains its own data and methods. For example, you could
create a class called *Person” that has properties such as name and age, and methods such as
speak() and walk). Each instance of the Person class would be a unique object with its own name and
age, but they would all have the same methods to speak and walk.

One of the key features of OOP in Python is encapsulation, which means that the internal state of an
object is hidden and can only be accessed or modified through the object's methods. This helps to
protect the object's data and prevent it from being modified in unexpected ways.
'''
# Example :-

'''
RailwayForm ---> Class [blueprint]
DJ --> Object [entity]
Raj --> Object [entity]
ROhan --> Object [entity]
'''

class person :
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = person()
a.name = "Shubham"
a.occupation = "Accountant"
a.networth = 20
print(a.name)
print(a.occupation)
print(a.networth)
a.info()
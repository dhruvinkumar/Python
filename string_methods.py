# Strings are immuable
a = "!!!Rohit! !Rohit!!!"
print(len(a))
print(a.upper())
print(a)    # here we get original string only because string is immutable and all function return the copy of string they are not making changes in original one
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Rohit","Rohan"))
print(a.split(" "))
print(a.count("Rohit"))

blogHeaing = "introduction tO jS"
print(blogHeaing.capitalize()) # make only first character as uppercase rest all will be in lower case

str1 = "Welcome to the Console!!!"
print(str1.endswith("too",4,10))
print(len(str1))
print(len(str1.center(50)))

str1 = "He's name is Dan. He is an honset man."
print(str1.find("is")) # This will give first index of that if not found it will return -1
print(str1.index("is")) # This is same as find but if not found this will return error

str1 = "WelcometotheConsole" 
str2 = "Welcome to the Console!!!"
print(str1.isalnum())  # contain A-Z,a-z,0-9
print(str2.isalnum())
print(str1.isalpha()) # contain A-Z,a-z
print(str2.isalpha()) 

str1 = "Hello World"
print(str1.islower())
print(str1.isupper())

str1 = "We wish you a \"Merry Christmas\"\n"
str2 = "We wish you a \"Merry Christmas\""
print(str1.isprintable())
print(str2.isprintable())

str1  = "     "
print(str1.isspace())

str1 = "World Health Organization"
str2 = "World health organization"
print(str1.istitle()) # Check weather each starting character of word is capital or not
print(str2.istitle())
print(str2.title()) 

str1 = "Python is a Interpreted Language"
print(str1.startswith("Pyton"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())
class person :
    name = "DJ"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = person()
b = person()
c = person()

a.name = "Shubham"
a.occupation = "Accountant"
a.networth = 20


b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
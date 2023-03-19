class person:
    def __init__(self, name, occ):
       print("Hey I am a person")
       self.name = name
       self.occ = occ
       
    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Divya","HR")
b = person("DJ","Developer")
# print(a.name)
# a.name  = "Divya"
# a.occ = "HR"
a.info()
b.info()

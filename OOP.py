class EmobilisStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
         print(f"my name is {self.name} and am {self.age} years old")

#creating object]
myobj=EmobilisStudent("Victor",30)
myobj.hello_me()

# create a class call magari, it should have model,make,year properties

class Magari:
    def __init__(self,model,year,make,properties):
        self.model=model
        self.year=year
        self.make=make
        self.properties=properties
    def hello_me(self):
        print(f"This is a {self.model} manufactured in {self.year} it is a {self.make} and can go up to speeds o"f" {self.properties}")

#creating object
myobj=Magari("Mercedes",2009,"Maybach",360)
myobj.hello_me()
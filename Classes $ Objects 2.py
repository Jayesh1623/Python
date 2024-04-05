# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class person():
    def __init__(self,n,o):
        # print("Hey I am a person")
        self.name= n
        self.role= o
        
    def info(self):
        print(f"{self.name} is a {self.role}"),
  
  
  
a= person("Jayesh", "HR.")
b= person("Aman", "React developer.")

a.info()
b.info()

# the self parameter is a reference to the current instance of the class, and is used to 
# access variables that belong to the class.

# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# Modify Object Properties

class person:
   def __init__(self,name,age):
    self.name= name
    self.age=age
   
   def myfunt(self):
       print(f"My name is {self.name}")
   
p1= person("Jayesh",28)
p1.name= "Aman"
p1.myfunt()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)



# delete object

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)

class person():
    name= "Jayesh"
    role= "RPA developer"
    city= "pune"
    def info(self):
        print(f"{self.name} is a {self.role}")
  
  
  
a= person()
b= person()
c= person()


a.name= "Aman" 
# print(a.name)

b.name= "Rahul"
b.role= "Python developer"

a.info()

b.info()
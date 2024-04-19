class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def ShowdDetails(self):
        print(f"The name of employee: {self.id} is {self.name}.")
 
   
class programmer(employee):
    def ShowLanguage(self):
        print("The default laungauage is Python.")   
 
     
e1 = employee("Jayesh", 45)
e1.ShowdDetails()
# e1.ShowLanguage()

e2 = programmer("Aman", 18)
e2.ShowLanguage() 
e2.ShowdDetails()


"Public Variables"

# class Employee():
#     def __init__(self):
#         self.name= 'harry'
        
# k= Employee()
# print(k.name)




"Private varaibles"

class Employee():
    def __init__(self):
        self.__name= 'harry'
        
k= Employee()
# print(k.__name)
print(k._Employee__name)  # Name Mangling
print(k.__dir__())
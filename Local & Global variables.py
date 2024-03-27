# x= 6  # global varible

# def my_function():
#     y=8
#     print(y)  #local variable
#     print(x) # we can access global variable in function.
    
# my_function()

# print(x)   # gloabl variable
# print(y)   # local variable this will cause error because local variable
#is defined in function only and not accesible outside the function.




x= 6 

def my_function():
    y=8
    global x
    x=2
    print(y) 
    
    
my_function()

print(x) 
def CalculateMean(a,b):
     Mul=(a*b)
     Add=(a+b)
     mean=Mul/Add
     print(mean)
     
CalculateMean(3,5)
     
def Isgreater(a,b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")   
        
Isgreater()
     

a = 9
b = 8

mean = (a*b)/(a+b)
print ( mean )

c=8
d=7

mean=(c*d)/(c+d)
print(mean)


a = 5
b = 4

if (a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal")
        
CalculateMean(a,b)

a = 3
b = 4

Isgreater(a,b)
CalculateMean(a,b)


# Use this as seperator

def average(a=2,b=3):
    print("The average is", (a+b)/2)
    

average(b=4)

average(5)

average()
 



def name(fname,mname,lname):
    print("Hello", fname, mname, lname)
    
name("Jayesh", "Nago","Patil")



def name(fname="Jayesh",mname="X",lname="patil"):
    print("Hello", fname, mname, lname)
    
name(lname="Pawar")
    

def total(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print(sum)
        
total(5,6,7,8)

print("Separator")

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


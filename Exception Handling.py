a= input("Enter the number: ")

print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except ValueError:
    print("Input is not in number format")
print("Some lines of code")
print("End of program")


try:
    b= int(input("Enter the number: "))
    c= [4,6,7]
    print(c[b])

except ValueError:
    print("Invalid number")

except IndexError:
    print("Invalid index")




def funt1():
  try:  
    m= [1,5,8,6]
    i=int(input("Enter the index: "))
    print(m[i])
    return 1
  except:
    print("Invalid index")
    return 0
  finally:
    print("I am always executed")
    
  print("I am always")
    
x= funt1()
print(x)

#  Exception Handling

t= int(input("Enter the number between 5 and 9 :"))

if t<5 or t>9:
    raise ValueError ("Value should between 5 and 9")
else:
    print("All Good") 
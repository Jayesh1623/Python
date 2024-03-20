Age= int(input("Enter your age :"))
print(Age)

if(Age>=18):
 print("Great! you can drive.")
else:
 print("Sorry!, you cannot drive.") 
 
 print(Age<18)
 print(Age<=18)
 print(Age>=18)
 print(Age>18)
 print(Age==18)
 print(Age!=18)


print("For elif")
num = -1
if (num< 0):
    print("Number is less than zero")
elif (num>0):
    if (num <= 10):
        print("Number is between 1 to 10")
    elif (num>10 and num<=20):
        print("Number is between 1 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

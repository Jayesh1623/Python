X = int(input("Enter the number off your choice :"))
 
match X:
    case 0:
        print("Number is zero")
    case 5:
        print("Number is 5") 
    case _ if X !=12:
        print("Not Matched 12")      
    case _ if X !=18:
        print("Not Matched 18")     
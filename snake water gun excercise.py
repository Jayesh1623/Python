import random

def check(comp, user):
    if (comp == user):
     return 0 

    elif (comp == 0 and user_input == 1):
        return -1
 
    elif (comp == 1 and user_input == 2):
        return -1
    elif (comp == 2 and user_input == 0):
        return -1

    return 1


comp = random.randint(0,2)
print("you: ", user_input)
print("Computer: ", comp)  
    print("Its a Draw")
elif score == -1: 
    print("You Lost")
else:
    print("You Won")
  
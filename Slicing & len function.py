'''Slicing and use of lenght function
Indexing of any data starts from Zero in python.
If we parse any data using index then it returns Index minus 1 data starting from zero.'''

Fruit=("Mango")

FruitLenght=(len(Fruit))

print(FruitLenght)

print(Fruit[0:3]) 
# Include 0 index but not 3 

print(Fruit[:3])
# Python interpreter automatically consider zero if we are not giving any value.

print(Fruit[0:])
# Python automatically prints full word if we are not giving to lenght.

print(Fruit[0:-3])
# Python subtracts the negative index from the length of the data. like print(Fruit[0:len(Fruit)-3].

print(Fruit[-4:-2])
# print(Fruit[len(Fruit)-4:len(Fruit)-2]
# print(Fruit[5-4:5-2]
# print(Fruit[1:3]
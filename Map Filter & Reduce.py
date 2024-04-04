def cube(x):
    return x*x*x

print(cube(2))


k= [2,3,5,6,4,3]

# newlist=[]

# for a in k:
#     newlist.append(cube(a))
    
# print(newlist)

# newlist = list(map(cube, k))
# print(newlist)

newlist = list(map(lambda x: x*x*x, k))
print(newlist)


# Filter

def filter_function(x):
    return x>4

# list1 = list(filter(filter_function, k))
# print(list1)
    
list1 = list(filter(lambda r: r>4, k))
print(list1)


# Reduce

from functools import reduce

numbers= [2, 3, 5, 6 ,9, 7]

def my_funct(x,y):
    return x+y

# sum = reduce(my_funct, numbers)
# print(sum)

sum = reduce(lambda x,y:x+y , numbers)
print(sum)

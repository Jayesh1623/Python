# Sets are unordered collection of items in which items are not reapeated 
# store multiple items in single varaible and are enclosed in curly braces seperated by comma.

# a={2,4,2,6,4,8}
# print(a)

# can store items of different data types in same set & order is not maintained.
# We cannot access set items by using index because set order is not fix.
# set does not allow duplicate values.

# k = {"jayesh", 45, 5.9, False, 45}
# print(k)

# harry= set()

# print(type(harry))

# for value in k:
#     print(value)
    
    
s1= {2,5,6,7}
s2= {7,8,9}

print(s1, s2)

print(s1.union(s2))

print(s1.intersection(s2))

s1.update(s2)
print(s1)


s1= {2,5,6,7}
s2= {7,8,9}

print(s1.symmetric_difference(s2))

cities1= {"pune", "mumbai", "Nasik", "Nagpur", "Banguluru"}
cities2= {"mumbai", "satara", "jalgaon"}
print(cities1.difference(cities2))

print(cities1.isdisjoint(cities2))

print(cities1.issuperset(cities2))

print(cities1.issubset(cities2))

cities1.add("Kabul")
print(cities1)

cities1.remove("Nasik")
print(cities1)

# cities1.remove("Dhule")    '''remove throws error while discard don't throw error'''
# print(cities1)

cities1.discard("Dhule")
print(cities1)

print(cities1.pop())

k= {1,3,5}

print(k)

# del k '''it will delete the set k'''

# print(k)

k= {1,3,5}

k.clear
print(k)

if 3 in k:
    print("3 is present in set \"k\"")
else:
    print("3 is not present in set \"k\"")
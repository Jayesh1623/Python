a= [9, 1, 7, 6 ,8]
b= [8, 5, 9, 7 ,2]

c=a+b
print(c)


for x in b:
    a.append(x)
print(a)


a.extend(b)
print(a)
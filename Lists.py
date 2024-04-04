marks=[65,78,87,96,59]


print(len(marks))
print(type(marks))
print(marks[(len(marks)-1)])
print(marks)
print(marks[:]) 
print(marks[1:])
print(marks[:3])
# lenght of marks -3
print(marks[1:-3])
# jump index
print(marks[1:5:2])



A=0
for i in marks:
  print(marks[A])
  A = A+1
else:
    print("exit")
    
for i in marks:
    print(i)
    
print(marks[0])
print(marks[2])

if 65 in marks:
    print("yes")
else:
    print("no")

for i in marks :
    if i<70:
     print("yes")
     print(i)
    else:
     print("no")

print("For end")
for i in range(10):
    print(i)

print("For end")
for i in range(10):
    print(i+1)

print("For start and end")
for i in range(1, 10):
    print(i)

print("For start, end & step")
for i in range(1, 12, 2):
     print(i)


for name in ["Jayesh", "Aman", "Yash", "Aadi", "Veera", "Dhiraj"]:
    print(name)
    for i in name:
        print(i)

Colour= "Orange"
for i in Colour:
    print(i)


No = 10

while No < 20:
    print(No)
    No = No+1
else:
    if No >= 20:
        print(No+1)


Number = int(input("Enter the number:"))

while Number <= 20:
    Number = int(input("Enter the number:"))

print("Done with the loop")

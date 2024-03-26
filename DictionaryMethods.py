students1={"Aman": 456, "Yash": 565, "Veera": 522, "Aadi": 499}

students2= {"Shreyash":476, "Akshay": 410}

students1.update(students2)
print(students1)

# students1.clear()
# print(students1)

Jp={}
print(Jp)

students1.pop("Yash")
print(students1)

students1.popitem()
print(students1)

# del students1  """ It deletes the dictionary students1 so print will give error """
# print(students1)

del students2["Akshay"]
print(students2)
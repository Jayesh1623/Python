Dict= {
    "Aman" : "Best friend",
    "yash" : "School friend",
    "veera" : "College friend",
    "Shubham" : "Area friend" 
}
print(type(Dict))
print(Dict)
print(Dict["Shubham"])
 
EMID= {
    "Jayesh" : "1623",
    "Akshay" : "1487",
    "Shreyash" : 1626,
    "Shamali" : 1620,
    "Rushi" : 1567
}

print(type(EMID))
print(EMID["Shreyash"])      
      
# ''' throws error if key not matched '''

print(EMID.get('Shreyash'))   

# ''' returns none if key not matched '''

for i in EMID:
    print(i,":",EMID[i])
    if i == "Akshay":
        k=(EMID[i])
        print(k)
        break
    
print(f"Hello the Employee ID of akshay is {k}")

for i in EMID.keys():
    print(f"The value corresponding to {i} is {EMID[i]}.")
    
print(EMID.items())

for k in EMID.items():
    print(k)
    
for key, value in EMID.items():
       print(f"The value corresponding to {key} is {value}.")
       
for j in EMID:
    print(j)
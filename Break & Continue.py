for i in range(12):
    if (i==10):
        break
    else:
        print("5 *",i+1,"=", 5 *(i+1))
        
for i in range(12):
    if (i==10):
        continue
    else:
        print("5 *",i,"=", 5 *(i))
         
         

i=100
while True:
    print(i)
    # i=i+1
    if (i % 100 == 0):
      break
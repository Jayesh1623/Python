marks= [78,60,96,65,48]

# index=0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#       print("Top marks")
#     index=index+1
    

# we can get index by using enumerate function.
# for index, mark in enumerate(marks):
#     print(mark)
#     if(index == 2):
#       print("Top marks")
      
# we can give specific start index if needed
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 2):
      print("Top marks")

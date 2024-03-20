import time
Timestamp = time.strftime('%H:%M:%S')
print(Timestamp)

print(type(Timestamp))

A = int(Timestamp[0:2])
print(A)

print(type(A))

# A=int(time.strftime('%H'))

if (A >= 12 and A < 18):
    print("Good Afternoon Everyone!!!")
elif (A >= 18):
    print("Good Evening Everyone!!!")
else:
    print("Good Morning Everyone!!!")

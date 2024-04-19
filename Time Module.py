import time 

# def funct1():
#     i = 0
#     while i<5000:
#         print(i)
#         i=i+1
        
# def funct2():
#     for k in range(5000):
#         print(k)
        
        
# init= time.time()
# funct1()
# a = time.time()-init

# time.sleep(5)

# init=time.time()
# funct2()
# print(f"first time is {a}")
# print(f"Second time is {time.time()-init}")

t=time.localtime()
formated_time= time.strftime("%d-%m-%y %H:%M:%S",t)
print(formated_time)
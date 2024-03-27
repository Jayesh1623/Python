
a= open('myfile.txt', 'r')

text= a.read()
print(text)
a.close()

f= open('myfile.txt', 'a')
f.write(': Hello world')
f.close()

# f= open('myfile.txt', 'w')  # if file not present then 'w' mode will create that file & then write in it.
# f.write('Hello world')
# f.close()

# with open('myfile.txt', 'a') as a:    # with this we can open file and we don't need to use close.
#     a.write("hello")
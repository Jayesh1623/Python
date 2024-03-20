l = [ 93, 33, 78, 59, 66, 12, 3]

print(l)

l.append(7)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

# After sorting
print(l.index(78))

print(l.count(12))

l[2]=100

print(l)

m = l.copy()
m[3] = 209
print(l)
print(m)

m.insert( 4, 99 )
print(m)

n= [300,400,500]
m.extend(n)
print(m)

k=l+m
print(k)
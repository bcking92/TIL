a = 'abcdef'
b = []
for i in range(len(a)):
    b.append(a[i])

c = {}

for i in range(len(b)) :
    c[b[i]] = i
    print(b[i] + ": "+ str(i))
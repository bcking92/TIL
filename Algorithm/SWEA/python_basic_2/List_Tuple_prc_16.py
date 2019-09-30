a = input()
b = a.split(', ')
b = [int(x) for x in b ]
c = tuple(b)
print(b)
print(c)
a = int(input())
b = []
for i in range(a):
    b.append(input())

for j in range(len(b)):
    c = 0
    for k in range(1000):
        if b[j].split[' '].count(b[j].split[' '][k]) > c:
            d = b[j].split[' '][k]
            c = b[j].split[' '].count(b[j].split[' '][k])
        elif b[j].split[' '].count(b[j].split[' '][k]) == c:
            if d <= b[j].split[' '][k]:
               	c = b[j].split[' '].count(b[j].split[' '][k])
               	d = d = b[j].split[' '][k]
       	else:
           	continue
    print('#{0} {1}'.format(j+1,c))
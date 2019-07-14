a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
b = list(a)
c = ''
for i in range(len(b)) :
    if b[i] != 'a' and b[i] != 'e' and b[i] != 'u' and b[i] != 'i' and b[i] != 'o' :
        c += b[i]
print(c)
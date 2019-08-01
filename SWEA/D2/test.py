a = '-12-35+1222'+' '
b = []
c = ''
for i in a:
    if i.isdigit():
        c += i
    else:
        b.append(c)
        c = '' + i
b.remove('')
cal = 0
for i in b:
    cal += int(i)
print(cal)
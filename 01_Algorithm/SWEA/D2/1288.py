a = int(input())
for i in range(a):
    b = int(input())
    n = 1
    c = set(str(b))
    while True:
        n += 1
        d = n*b
        c = c.union(set(str(d)))
        if c == {'0','1','2','3','4','5','6','7','8','9'}:
            break
    print('#{0} {1}'.format(i+1,b*n))


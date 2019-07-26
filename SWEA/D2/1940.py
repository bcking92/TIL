a = int(input())
for i in range(a):
    b = int(input())
    z = 0
    for j in range(b):
        c = input().split(' ')     
        for k in range(c[1]):
            print(c[0], end='')
            z += 1
            if z == 10:
                print()
                z = 0
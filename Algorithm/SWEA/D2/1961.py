test = int(input())
for t in range(test):	
    n = int(input())
    li = []
    for h in range(n):
        li.append(input().split(' '))
    for m in range(n):
        for i in range(n):
            print(li[n-i-1][m], end= '')
            print(' ',end= '')
        for k in range(n):
            print(li[n-m-1][n-k-1], end='')
            print(' ',end= '')
        for j in range(n):
            print(li[j][n-m-1], end='')
test = int(input())

for i in range(test):
    num, A, B = list(map(int,input().split(' '))), list(map(int,input().split(' '))), list(map(int,input().split(' ')))
    li = []
    if num[0] > num[1]:
        for j in range(num[0]-num[1]+1):
            s = 0
            for k in range(num[1]):
                s += A[k+j] * B[k]
            li.append(s)
    elif num[0] < num[1]:
        for m in range(num[1]-num[0]+1):
            s = 0
            for n in range(num[0]):
                s += A[n] * B[n+m]
            li.append(s)
    else:
        for q in range(num[0]):
            s += A[q] * B[q]
       	li.append(s)
    print('#{0} {1}'.format(i+1,max(li)))
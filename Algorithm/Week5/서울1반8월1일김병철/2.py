import sys

sys.stdin = open('input2.txt','r')

def bus(K,x):
    result = 0
    me = 0
    x1= [0]
    idx = 0
    while me < x[-1]:
        if me + K < x[idx]:
            return 0
        else:
            for j in x:
                if me + K >= j and j >= x[idx]:
                    x1 += [j]
                    idx += 1
        me = x1[-1]
        result += 1
    return result -1

for i in range(int(input())):
    K,N,M = tuple(map(int,input().split()))
    x = list(map(int,input().split())) + [N]
    print('#{} {}'.format(i+1,bus(K,x)))

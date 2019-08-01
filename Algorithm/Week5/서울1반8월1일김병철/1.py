import sys

sys.stdin = open('input.txt', 'r')

def my_max(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x[-1] - x[0]

for i in range(int(input())):
    a,b = int(input()), list(map(int,input().split()))
    print('#{} {}'.format(i+1,my_max(b)))
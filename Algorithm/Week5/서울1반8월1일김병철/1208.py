import sys

sys.stdin = open('Flatten.txt','r')

def my_sort(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1], x[j]
    return x

for i in range(10):
    num = int(input())
    x = list(map(int,input().split()))
    for j in range(num):
        x = my_sort(x)
        x[0] +=1
        x[-1] -=1
    x = my_sort(x)
    print('#{} {}'.format(i+1,x[-1]-x[0]))
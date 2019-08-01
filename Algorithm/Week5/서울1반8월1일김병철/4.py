import sys

sys.stdin = open('input4.txt','r')

def sum_gap(x,num):
    sum_arr = []

    for i in range(len(x)-num+1):
        sum_num = 0
        for j in range(num):
            sum_num += x[i+j]
        sum_arr = sum_arr + [sum_num]

    for i in range(len(sum_arr)-1,0,-1):
        for j in range(i):
            if sum_arr[j] > sum_arr[j+1]:
                sum_arr[j],sum_arr[j+1] = sum_arr[j+1],sum_arr[j]

    return sum_arr[-1] - sum_arr[0]

for i in range(int(input())):
    b, c = list(map(int,input().split()))[1], list(map(int,input().split()))
    print('#{} {}'.format(i+1,sum_gap(c,b)))
import sys

sys.stdin = open('input.txt','r')

def arr_max(x):
    my_max = 0
    temp3 = 0
    temp4 = 0
    for i in range(100):
        temp1 = 0
        temp2 = 0
        temp3 += x[i][i]
        temp4 += x[i][99 - i]
        for j in range(100):
            temp1 += x[i][j]
            temp2 += x[j][i]
        if my_max < temp1:
            my_max = temp1
        if my_max < temp2:
            my_max = temp2
    if my_max < temp3:
        my_max = temp3
    if my_max < temp4:
        my_max = temp4
    return my_max


for i in range(10):
    input()
    arr = []
    for j in range(100):
        arr.append(list(map(int, input().split())))
    print('#{} {}'.format(i + 1, arr_max(arr)))
import sys

sys.stdin = open('input.txt', 'r')

def my_sum(a, b):
    result = 0
    for x in range(len(a)-b+1):
        for y in range(len(a[0])-b+1):
            temp = 0
            for i in range(b):
                temp += a[x][y + i]
                temp += a[x + b-1][y + i]
            for i in range(b-2):
                temp += a[x + 1 + i][y]
                temp += a[x + 1 + i][y + b - 1]
            if temp > result:
                result = temp
    return result


for T in range(int(input())):
    N, M, K = map(int,input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().split())))
    print('#{} {}'.format(T+1, my_sum(matrix, K)))
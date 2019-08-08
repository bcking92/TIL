import sys

sys.stdin = open('input.txt', 'r')


for i in range(int(input())):
    N = int(input())
    mtx = []
    result = 0
    for j in range(N):
        mtx.append(list(map(int, input())))
    for j in range(N):
        if j < int((N + 1) / 2):
            start = int(N/2)-j
            for k in range(start, N - start):
                result += mtx[j][k]
        else:
            start = j - int(N / 2)
            for k in range(start, N - start):
                result += mtx[j][k]

    print('#{} {}'.format(i + 1, result))
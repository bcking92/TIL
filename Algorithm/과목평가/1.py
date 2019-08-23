import sys

sys.stdin = open('1.txt', 'r')

for T in range(int(input())):
    N, M = map(int,input().split())
    matrix = [[0]*N for i in range(N)]
    result = 0
    for i in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(min(x1,x2),max(x1,x2) + 1):
            for y in range(min(y1,y2),max(y1,y2) + 1):
                matrix[x][y] = 1
    for i in range(N):
        result += sum(matrix[i])

    print('#{} {}'.format(T+1, result))
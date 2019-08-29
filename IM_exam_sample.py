import sys

sys.stdin = open('input.txt', 'r')

for T in range(int(input())):
    N, M, K = map(int, input().split())
    colorq = [0 for i in range(11)]
    matrix = [[0] * M for i in range(N)]
    for i in range(K):
        chill = True
        x1, y1, x2, y2, color = map(int, input().split())
        for j in range(min(x1, x2), max(x1, x2) + 1):
            for k in range(min(y1, y2), max(y1, y2) + 1):
                if matrix[j][k] > color:
                    chill = False
                    break
        if chill:
            for a in range(min(x1, x2), max(x1, x2) + 1):
                for b in range(min(y1, y2), max(y1, y2) + 1):
                    matrix[a][b] = color

    for i in range(N):
        for j in range(M):
            colorq[matrix[i][j]] += 1

    print('#{} {}'.format(T + 1, max(colorq)))

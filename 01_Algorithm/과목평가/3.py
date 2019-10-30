import sys

sys.stdin = open('3.txt', 'r')

dx = [0, 1, 1 ,1 , 0 , -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

# 재귀로 풀기

# def infection(x, start_x, start_y, island):
#         x[start_x][start_y] = island
#         for i in range(8):
#             if start_x + dx[i] in range(N) and start_y + dy[i] in range(N):
#                 if 0 < x[start_x + dx[i]][start_y + dy[i]] <= 50:
#                     infection(x, start_x + dx[i], start_y + dy[i], island)
#
# for T in range(int(input())):
#     N = int(input())
#     matrix = []
#     for i in range(N):
#         matrix.append(list(map(int,input().split())))
#
#     cnt = 51
#     for i in range(N):
#         for j in range(N):
#             if 0 < matrix[i][j] <= 50:
#                 infection(matrix, i, j, cnt)
#                 cnt += 1
#
#     print('#{} {}'.format(T+1, cnt-51))
#
#
#
# 반복문 + stack으로 풀기

for T in range(int(input())):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    stack = []
    cnt = 51
    for i in range(N):
        for j in range(N):
            if 0 < matrix[i][j] <= 50:
                stack.append([i, j])
                while stack:
                    start_x, start_y = stack[-1][0], stack[-1][1]
                    matrix[start_x][start_y] = cnt
                    for k in range(8):
                        if start_x + dx[k] in range(N) and start_y + dy[k] in range(N):
                            if 0 < matrix[start_x + dx[k]][start_y + dy[k]] <= 50:
                                start_x += dx[k]
                                start_y += dy[k]
                                stack.append([start_x, start_y])
                                break
                    else:
                        stack.pop()

                cnt += 1

    print('#{} {}'.format(T + 1, cnt - 51))

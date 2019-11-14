import sys

sys.stdin = open('sample_input.txt', 'r')

direction_out = [
    ((0, 0)),
    ((0, 1), (0, -1), (1, 0), (-1, 0)),
    ((1, 0), (-1, 0)),
    ((0, 1), (0, -1)),
    ((-1, 0), (0, 1)),
    ((1, 0), (0, 1)),
    ((1, 0), (0, -1)),
    ((-1, 0), (0, -1))
    ]

def dfs(x, y, now, t, visited):
    global chief_area
    if now == t:
        return
    for dx, dy in direction_out[arr[x][y]]:
        temp_x, temp_y = x + dx, y + dy
        if 0 <= temp_x < N and 0 <= temp_y < M:
            if (temp_x, temp_y) not in visited :
                if (-dx, -dy) in direction_out[arr[temp_x][temp_y]]:
                    chief_area[temp_x][temp_y] = 1
                    dfs(temp_x, temp_y, now+1, t, visited + [(temp_x, temp_y)])

for T in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    arr = [tuple(map(int, input().split())) for i in range(N)]
    chief_area = [[0] * M for i in range(N)]
    chief_area[R][C] = 1
    dfs(R,C, 1, L, [(R, C)])
    result = 0
    for i in range(N):
        result += sum(chief_area[i])
    print('#{} {}'.format(T+1, result))

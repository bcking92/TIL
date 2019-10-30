def dfs(temp, x, y, num):
    stack = [(x, y)]
    while stack:
        t = stack.pop()
        temp[t[0]][t[1]] = num
        for i in range(4):
            temp_x = t[0] + dx[i]
            temp_y = t[1] + dy[i]
            if 0 <= temp_x < N and 0 <= temp_y < N:
                if 0 < temp[temp_x][temp_y] < 101:
                    stack.append((temp_x, temp_y))


dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
N = int(input())
land = []
highest = 0
result = 1
lowest = 100
for i in range(N):
    land.append(list(map(int, input().split())))
for i in range(N):
    a = max(land[i])
    b = min(land[i])
    if a > highest:
        highest = a
    if b < lowest:
        lowest = b
for i in range(lowest, highest):
    num = 101
    for j in range(N):
        for k in range(N):
            if 0 < land[j][k] <= i:
                land[j][k] = 0

    new = [land[i].copy() for i in range(N)]
    for j in range(N):
        for k in range(N):
            if 0 < new[j][k] < 101:
                dfs(new, j, k, num)
                num += 1
    num -= 101
    if result < num:
        result = num

print(result)
def dfs(x, y, c, n, m):
    stack = [(x, y)]
    visited = {}
    while stack:
        x, y = stack.pop()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if c <= temp_x < n and c <= temp_y < m:
                if not cheese[temp_x][temp_y]:
                    if not visited.get((temp_x, temp_y)):
                        visited[(temp_x, temp_y)] = 1
                        stack.append((temp_x, temp_y))
                else:
                    cheese[temp_x][temp_y] = 2


dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

N, M = map(int, input().split())
cheese = []
visited = {}
hours = 0
go = 1
hour_ago_left_cheese = 0
left_cheese = 0

a = 0
b = 0
for i in range(N):
    cheese.append(list(map(int, input().split())))

for i in range(N):
    left_cheese += sum(cheese[i])
while True:
    hours += 1
    hour_ago_left_cheese = left_cheese
    left_cheese = 0
    dfs(a, b, a, N, M)
    for j in range(a, N):
        for k in range(b, M):
            if cheese[j][k] == 2:
                cheese[j][k] = 0
    for j in range(N):
        a = sum(cheese[j])
        left_cheese += a

    if not left_cheese:
        break
    a += 1
    b += 1
    N -= 1
    M -= 1
print(hours)
print(hour_ago_left_cheese)
# for i in range(13):
#     print(cheese[i])

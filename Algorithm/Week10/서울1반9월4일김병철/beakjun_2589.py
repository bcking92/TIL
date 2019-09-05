dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

N, M = map(int, input().split())
island = []
result = 0
queue = []
start = []
for i in range(N):
    island.append(input())
island = tuple(island)
for i in range(N):
    for j in range(M):
        if island[i][j] == 'L':
            # bfs(island, i, j, 0)
            start.append((i, j))

for i, j in start:
    queue.append((i, j, 0))
    visited = {}
    visited[(i, j)] = 1
    while queue:
        x, y, c = queue.pop(0)
        for k in range(4):
            temp_x = x + dx[k]
            temp_y = y + dy[k]
            if 0 <= temp_x < N and 0 <= temp_y < M:
                if island[temp_x][temp_y] == 'L':
                    if not visited.get((temp_x, temp_y)):
                        visited[(temp_x, temp_y)] = 1
                        queue.append((temp_x, temp_y, c + 1))
    if result < c:
        result = c
print(result)



def safe_area():
    global N, M
    visited = {}
    stack = []
    for i in virus:
        stack.append(i)
        visited[i] = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp_x = x + dx
            temp_y = y + dy
            if 0 <= temp_x < N and 0 <= temp_y < M:
                if jido[temp_x][temp_y] == '0':
                    if not visited.get((temp_x, temp_y)):
                        visited[(temp_x, temp_y)] = 1
                        stack.append((temp_x, temp_y))
    aaa = N * M - wall - len(visited) - 3
    return aaa


N, M = map(int, input().split())
jido = []
wall_candidate = []
virus = []
wall = 0
result = 0
for i in range(N):
    jido.append(input().split())

for i in range(N):
    for j in range(M):
        if jido[i][j] == '0':
            wall_candidate.append((i, j))
        elif jido[i][j] == '2':
            virus.append((i, j))
        else:
            wall += 1
len_candidate = len(wall_candidate)
combis = []

for i in range(len_candidate - 2):
    for j in range(i, len_candidate - 1):
        for k in range(j, len_candidate):
            combis.append((wall_candidate[i], wall_candidate[j], wall_candidate[k]))

for i in combis:
    jido[int(i[0][0])][int(i[0][1])] = '1'
    jido[int(i[1][0])][int(i[1][1])] = '1'
    jido[int(i[2][0])][int(i[2][1])] = '1'
    a = safe_area()
    jido[int(i[0][0])][int(i[0][1])] = '0'
    jido[int(i[1][0])][int(i[1][1])] = '0'
    jido[int(i[2][0])][int(i[2][1])] = '0'
    if result < a:
        result = a
print(result)

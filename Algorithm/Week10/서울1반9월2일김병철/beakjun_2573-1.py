direction = ((0, -1), (0, 1), (1, 0), (-1, 0))
N, M = map(int, input().split())
ice_burg = [list(map(int, input().split())) for i in range(N)]
years = 0
end = 0
stack = []
visit = []
for i in range(N):
    for j in range(M):
        if ice_burg[i][j]:
            stack.append((i, j))
            visit.append((i, j))
while True:
    new = [[0] * M for _ in range(N)]

    years += 1
    visit = [stack[0]]
    while stack:
        x, y = stack.pop()
        new[x][y] = ice_burg[x][y]
        cnt = 0
        for i in range(4):
            temp_i = x + direction[i][0]
            temp_j = y + direction[i][1]
            if 0 <= temp_i < N and 0 <= temp_j < M:
                if 0 < ice_burg[temp_i][temp_j] < 200000:
                    stack.append((temp_i, temp_j))
                    visit.append((temp_i, temp_j))
                else:
                    cnt += 1
        new[x][y] -= cnt
        if new[x][y] < 0:
            new[x][y] = 0
        ice_burg[x][y] = 200000
    for x, y in visit:
        if 0 < ice_burg[x][y] < 20000:
            end = 1
            print(years)
            break
        if 0 < new[x][y]:
            stack = [(x, y)]
    if end:
        break
    if not stack:
        print(0)
        break
    ice_burg = new

"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 0 0 0 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0
"""
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
ice_berg = {}
years = 0
end = 0
N, M = map(int, input().split())
matrix = [tuple(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(M):
        height = matrix[i][j]
        if height:
            ice_berg[(i, j)] = height

while True:
    years += 1
    for k, v in ice_berg.items():
        x, y = k[0], k[1]
        for j in range(4):
            if ice_berg.get((x + dx[j], y + dy[j])) is None:
                ice_berg[(x, y)] -= 1
    new_berg = {}
    for k, v in ice_berg.items():
        if v > 0:
            new_berg[k] = v
    if not new_berg:
        print(0)
        break
    ice_berg = new_berg.copy()
    stack = [tuple(ice_berg.keys())[0]]
    while stack:
        k = stack.pop()
        new_berg[k] = 11
        temp_x, temp_y = k[0], k[1]
        for l in range(4):
            new_x, new_y = temp_x + dx[l], temp_y + dy[l]
            if ice_berg.get((new_x, new_y)):
                if new_berg[(new_x, new_y)] != 11:
                    stack.append((new_x, new_y))
    for v in new_berg.values():
        if v != 11:
            print(years)
            end = 1
            break
    if end:
        break



'''
5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 10 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 3 3 1 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
1


5 7
0 0 0 0 0 0 0
0 3 6 3 6 7 0
0 3 0 0 0 10 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2


5 7
0 0 0 0 0 0 0
0 3 6 0 6 7 0
0 3 0 0 0 10 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 9 8 3 8 9 0
0 9 8 0 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
5


5 5
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0
'''

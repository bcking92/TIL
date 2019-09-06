def permutation(x, end):
    global directions, CCTVs_direction

    if x == end:
        CCTVs_direction.append(tuple(directions))
    else:
        for k in direction:
            directions.append(k)
            permutation(x + 1, end)
            directions.pop()

N, M = map(int, input().split())
samusil = []
CCTVs = []
CCTVs_direction = []
directions = []
direction = (1, 2, 3, 4)
wall = 0
result = 1000
for i in range(N):
    samusil.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if 1 <= samusil[i][j] < 6:
            CCTVs.append((i, j))
        elif samusil[i][j] == 6:
            wall += 1

permutation(0, len(CCTVs))
camera1 = ((0, 1), (1, 0), (0, -1), (-1, 0))
camera2 = (((0, 1),(0, -1)), ((1, 0), (-1, 0)))
camera3 = (((0, 1), (-1, 0)), ((0, 1), (1, 0)), ((0, -1), (1, 0)), ((0, -1), (-1, 0)))
camera4 = (((0, 1), (-1, 0), (0, -1)), ((0, 1), (-1, 0), (1, 0)), ((0, 1), (1, 0), (0, -1)), ((-1, 0), (1, 0), (0, -1)))

for i in CCTVs_direction:
    visited = {}
    for j in range(len(CCTVs)):
        a = CCTVs[j][0]
        b = CCTVs[j][1]

        if samusil[a][b] == 1:
            x = a
            y = b
            visited[(x, y)] = 1
            dx, dy = camera1[i[j] - 1]
            while True:
                temp_x = x + dx
                temp_y = y + dy
                if 0 <= temp_x < N and 0 <= temp_y < M:
                    if not visited.get((temp_x, temp_y)):
                        if samusil[temp_x][temp_y] != 6:
                            visited[(temp_x, temp_y)] = 1
                        else:
                            break
                    x = temp_x
                    y = temp_y
                else:
                    break
        elif samusil[a][b] == 2:
            directions =  camera2[(i[j]+1) % 2]
            for dx, dy in directions:
                x = a
                y = b
                visited[(x, y)] = 1
                while True:
                    temp_x = x + dx
                    temp_y = y + dy
                    if 0 <= temp_x < N and 0 <= temp_y < M:
                        if not visited.get((temp_x, temp_y)):
                            if samusil[temp_x][temp_y] != 6:
                                visited[(temp_x, temp_y)] = 1
                            else:
                                break
                        x = temp_x
                        y = temp_y
                    else:
                        break
        elif samusil[a][b] == 3:
            for dx, dy in camera3[i[j] - 1]:
                x = a
                y = b
                visited[(x, y)] = 1
                while True:
                    temp_x = x + dx
                    temp_y = y + dy
                    if 0 <= temp_x < N and 0 <= temp_y < M:
                        if not visited.get((temp_x, temp_y)):
                            if samusil[temp_x][temp_y] != 6:
                                visited[(temp_x, temp_y)] = 1
                            else:
                                break
                        x = temp_x
                        y = temp_y
                    else:
                        break
        elif samusil[a][b] == 4:
            for dx, dy in camera4[i[j] - 1]:
                x = a
                y = b
                visited[(x, y)] = 1
                while True:
                    temp_x = x + dx
                    temp_y = y + dy
                    if 0 <= temp_x < N and 0 <= temp_y < M:
                        if not visited.get((temp_x, temp_y)):
                            if samusil[temp_x][temp_y] != 6:
                                visited[(temp_x, temp_y)] = 1
                            else:
                                break
                        x = temp_x
                        y = temp_y
                    else:
                        break
        elif samusil[a][b] == 5:
            for dx, dy in camera1:
                x = a
                y = b
                visited[(x, y)] = 1
                while True:
                    temp_x = x + dx
                    temp_y = y + dy
                    if 0 <= temp_x < N and 0 <= temp_y < M:
                        if not visited.get((temp_x, temp_y)):
                            if samusil[temp_x][temp_y] != 6:
                                visited[(temp_x, temp_y)] = 1
                            else:
                                break
                        x = temp_x
                        y = temp_y
                    else:
                        break
    temp = N * M - len(visited) - wall
    if temp < result:
        result = temp

print(result)




def bfs(x, y):
    global baby_shark, eat
    queue = [(x, y, 0)]
    visited = {(x, y) : 1}
    board[x][y] = 0
    caneat = []
    go = 1
    while queue:
        x, y, t = queue.pop(0)
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            temp_x = x + dx
            temp_y = y + dy
            if 0 <= temp_x < N and 0 <= temp_y < N:
                if not visited.get((temp_x, temp_y)):
                    if not board[temp_x][temp_y]:
                        if not caneat:
                            visited[(temp_x, temp_y)] = 1
                            queue.append((temp_x, temp_y, t + 1))
                    else:
                        if board[temp_x][temp_y] == baby_shark:
                            if not caneat:
                                visited[(temp_x, temp_y)] = 1
                                queue.append((temp_x, temp_y, t + 1))
                        elif board[temp_x][temp_y] < baby_shark:
                            caneat.append((temp_x, temp_y, t))
                            go = 0
        if not queue and not go:
            caneat = sorted(caneat, key=lambda x: (x[2], x[0], x[1]))
            temp_x, temp_y, t = caneat[0][0], caneat[0][1], caneat[0][2]
            queue = [(temp_x, temp_y,  t + 1)]
            eat += 1
            visited = {(temp_x, temp_y): 1}
            board[temp_x][temp_y] = 0
            c = t + 1
            go = 1
            caneat = []
            if eat == baby_shark:
                baby_shark += 1
                eat = 0

    if eat > 0 or baby_shark > 2:
        return c
    else:
        return 0

N = int(input())
board = []
baby_shark = 2
eat = 0
for i in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            start_x = i
            start_y = j
print(bfs(start_x, start_y))

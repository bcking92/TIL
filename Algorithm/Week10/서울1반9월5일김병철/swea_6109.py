left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

direction = (('left', left), ('right', right), ('up', up), ('down', down))

for T in range(int(input())):
    N, S = input().split()
    N = int(N)
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    for i in direction:
        if S == i[0]:
            dx, dy = i[1]
            break
    if S == 'up':
        for i in range(N):
            for j in range(N):
                x, y = i, j
                dt = 1
                now = board[x][y]
                while 0 <= x + dt < N and 0 <= y < N:
                    if board[x + dt][y]:
                        if board[x + dt][y] == now:
                            board[x][y] *= 2
                            board[x + dt][y] = 0
                            break
                        else:
                            break
                    dt += 1
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    x = i
                    y = j
                    while 0 <= x + dx < N and 0 <= y + dy < N:
                        if board[x + dx][y + dy] == 0:
                            board[x][y], board[x + dx][y + dy] = board[x + dx][y + dy], board[x][y]
                        x += dx
                        y += dy

    elif S == 'left':
        for i in range(N):
            for j in range(N):
                x, y = j, i
                dt = 1
                now = board[x][y]
                while 0 <= x < N and 0 <= y + dt < N:
                    if board[x][y + dt]:
                        if board[x][y + dt] == now:
                            board[x][y] *= 2
                            board[x][y + dt] = 0
                            break
                        else:
                            break
                    dt += 1
        for i in range(N):
            for j in range(N):
                if board[j][i]:
                    x = j
                    y = i
                    while 0 <= x + dx < N and 0 <= y + dy < N:
                        if board[x + dx][y + dy] == 0:
                            board[x][y], board[x + dx][y + dy] = board[x + dx][y + dy], board[x][y]
                        x += dx
                        y += dy
    elif S == 'down':
        for i in range(N):
            for j in range(N):
                x, y = N - 1 - i, j
                dt = -1
                now = board[x][y]
                while 0 <= x + dt < N and 0 <= y < N:
                    if board[x + dt][y]:
                        if board[x + dt][y] == now:
                            board[x][y] *= 2
                            board[x + dt][y] = 0
                            break
                        else:
                            break
                    dt -= 1
        for i in range(N):
            for j in range(N):
                if board[N - 1 - i][j]:
                    x = N - 1 - i
                    y = j
                    while 0 <= x + dx < N and 0 <= y + dy < N:
                        if board[x + dx][y + dy] == 0:
                            board[x][y], board[x + dx][y + dy] = board[x + dx][y + dy], board[x][y]
                        x += dx
                        y += dy
    else:
        for i in range(N):
            for j in range(N):
                x, y = j, N - 1 - i
                dt = -1
                now = board[x][y]
                while 0 <= x < N and 0 <= y + dt < N:
                    if board[x][y + dt]:
                        if board[x][y + dt] == now:
                            board[x][y] *= 2
                            board[x][y + dt] = 0
                            break
                        else:
                            break
                    dt -= 1
        for i in range(N):
            for j in range(N):
                if board[j][N - 1 - i]:
                    x = j
                    y = N - 1 - i
                    while 0 <= x + dx < N and 0 <= y + dy < N:
                        if board[x + dx][y + dy] == 0:
                            board[x][y], board[x + dx][y + dy] = board[x + dx][y + dy], board[x][y]
                        x += dx
                        y += dy
    print('#{}'.format(T + 1))
    for i in range(N):
        print(' '.join(map(str, board[i])))
    # for i in range(N):
    #     for j in range(N):



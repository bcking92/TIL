dx = (0, 0, 1, -1, 1, 1, -1, -1)
dy = (1, -1, 0, 0, 1, -1, 1, -1)

for T in range(int(input())):
    N, M = map(int, input().split())
    board = [[0] * N for i in range(N)]
    a = N//2 - 1
    b = N//2
    board[a][a] = 2
    board[b][b] = 2
    board[a][b] = 1
    board[b][a] = 1

    for i in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        for j in range(8):
            temp_x = x + dx[j]
            temp_y = y + dy[j]
            cnt = 0
            while True:
                if 0 <= temp_x < N and 0 <= temp_y < N:
                    if board[temp_x][temp_y] != 0 and board[temp_x][temp_y] != color:
                        cnt += 1
                        temp_x += dx[j]
                        temp_y += dy[j]
                    elif board[temp_x][temp_y] == color:
                        break
                    else:
                        cnt = 0
                        break
                else:
                    cnt = 0
                    break
            if cnt:
                for k in range(1, cnt+1):
                        board[x + dx[j] * k][y + dy[j] * k] = color
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(T + 1, black, white))





def greedy(x, y):
    global board, temp, result, save
    while True:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if board[x][y] + 1 == board[x + dx][y + dy]:
                    x += dx
                    y += dy
                    temp += 1
                    break
        else:
            break

for T in range(int(input())):
    N = int(input())
    board = [tuple(map(int, input().split())) for i in range(N)]
    result = 0
    now = 1
    for i in range(N):
        for j in range(N):
            temp = 1
            greedy(i, j)
            if temp > result:
                result = temp
                now = board[i][j]
            elif temp == result:
                if board[i][j] < now:
                    now = board[i][j]

    print('#{} {} {}'.format(T+1, now, result))
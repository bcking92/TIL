# def h_pop():
#     global arr
#     arr[len(arr)], arr[0] = arr[0], arr[len(arr)]
#     a = arr.pop()
#     while True:
#         if arr[0][]


dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def dijkstra(x, y):
    global memo, board, result, cnt
    arr = [(0, x, y)]
    memo[(x, y)] = 1
    while True:
        # cnt+= 1
        c, x, y = arr.pop(0)
        memo[(x, y)] = 1
        if x + y == 2 * (N - 1):
            result = c
            break
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < N and 0 <= temp_y < N:
                if not memo.get((temp_x, temp_y)):
                    if board[temp_x][temp_y] > board[x][y]:
                        arr.append((c + 1 + board[temp_x][temp_y] - board[x][y], temp_x, temp_y))
                    else:
                        arr.append((c+1, temp_x, temp_y))
                    l = len(arr) - 1
                    while True:
                        if arr[l][0] < arr[l//2][0]:
                            arr[l], arr[l//2] = arr[l//2], arr[l]
                        else:
                            break
for T in range(int(input())):
    N = int(input())
    board = tuple([tuple(map(int, input().split())) for i in range(N)])
    memo = {}
    result = 0
    cnt = 0
    dijkstra(0, 0)
    print('#{} {}'.format(T+1, result))
    # print(memo)
    # print(cnt)

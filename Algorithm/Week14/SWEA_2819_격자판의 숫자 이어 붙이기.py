def dfs(x, y):
    global board, visited
    stack = [(x, y, 0, '')]
    while stack:
        temp_x, temp_y, d, r = stack.pop()
        if d < 7:
            r += str(board[temp_x][temp_y])
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= temp_x + dx < 4 and 0 <= temp_y + dy < 4:
                    stack.append((temp_x + dx, temp_y + dy, d + 1, r))
        elif d == 7:
            if not visited.get(r):
                visited[r] = 1

for T in range(int(input())):
    board = [tuple(map(int, input().split())) for i in range(4)]
    visited = {}
    for i in range(4):
        for j in range(4):
            dfs(i, j)
    print('#{} {}'.format(T+1, len(visited)))
    print(visited)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = 1
for T in range(10):
    input()
    ladder = [input().split() for i in range(100)]
    x = 99
    for i in range(100):
        if ladder[x][i] == '2':
            y = i
            break
    while True:
        x += dx[direction]
        y += dy[direction]
        if x == 0:
            break
        if direction == 1:
            if 1<= y <= 98:
                if ladder[x][y-1] == '1':
                    direction = 3
                elif ladder[x][y+1] == '1':
                    direction = 2
                else:
                    continue
            elif not y:
                if ladder[x][y+1] == '1':
                    direction = 2
            else:
                if ladder[x][y-1] == '1':
                    direction = 3
        else:
            if y+dy[direction] in range(100) and ladder[x][y+dy[direction]] == '1':
                continue
            else:
                direction = 1
    print(f'#{T+1} {y}')
'''
# 뱀

1 = 사과
2 = 뱀
'''


N = int(input())
K = int(input())

dxdy = ((0,1), (-1,0), (0,-1), (1,0))
board = [[0] * N for i in range(N)]
snake_position = [[0,0]]
snake_direction = 0
snake_move = {}
time = 0

for i in range(K):
    x, y = map(int,input().split())
    board[x-1][y-1] = 1

L = int(input())

for i in range(L):
    a, b = input().split()
    snake_move[int(a)] = b

while True:
    time += 1
    new_head_x, new_head_y = snake_position[-1][0] + dxdy[snake_direction][0], snake_position[-1][1] + dxdy[snake_direction][1] 
    print(new_head_x, new_head_y)
    if 0 <= new_head_x <= N-1 and 0 <= new_head_y <= N-1:
        if [new_head_x, new_head_y] in snake_position:
            print(time) 
            break
        elif board[new_head_x][new_head_y] == 1:
            snake_position.append([new_head_x, new_head_y])
            board[new_head_x][new_head_y] = 0
        elif board[new_head_x][new_head_y] == 0:
            snake_position.append([new_head_x, new_head_y])
            snake_position.pop(0)
        if snake_move.get(time):
            if snake_move[time] == 'L':
                snake_direction = (snake_direction + 1) % 4
            else:
                snake_direction = (snake_direction - 1) % 4
    else:
        print(time)
        break 

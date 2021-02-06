'''
# 뱀

1 = 사과
2 = 뱀

뱀의 위치를 큐에 넣어서 구현
 - 머리가 이동하면 머리좌표를 큐에 push
    - 사과를 먹었다면 그대로 유지
    - 사과를 먹지 않았다면 pop(꼬리부분 잘라짐) 
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

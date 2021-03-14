N, M = map(int, input().split())
board = []
cand = []
real_virus = []
max_safety_zone = 0
for i in range(N):
    board.append(input().split())

for i in range(N):
    for j in range(M):
        if board[i][j] == '2':
            real_virus.append((i,j))

def calc_safe_area(in_board, added_walls, virus):
    result = 0
    for i, j in added_walls:
        in_board[i][j] = '1'
    for i, j in virus:
        stack = [(i,j)]
        while True:
            now_x, now_y = stack.pop()
            in_board[now_x][now_y] = '2'
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                if 0 <= now_x + dx < N and 0 <= now_y + dy < M and in_board[now_x+dx][now_y+dy] == '0':
                    stack.append((now_x+dx,now_y+dy))
            if not stack:
                break 
    for line in in_board:
        for block in line:
            if block == '0':
                result += 1
    return result

for i in range(N*M-2):
    if board[i//M][i%M] == '0':
        for j in range(i+1, N*M-1):
            if board[j//M][j%M] == '0':
                for k in range(j+1, N*M):
                    if board[k//M][k%M] == '0':
                        cand.append(((i//M, i%M),(j//M, j%M), (k//M, k%M)))

for real_added_walls in cand:
    temp_max_safety_zone = calc_safe_area([my_line[:] for my_line in board], real_added_walls, real_virus)
    if temp_max_safety_zone > max_safety_zone:
        max_safety_zone = temp_max_safety_zone


print(max_safety_zone)              
    
# print(calc_safe_area(board, ((1,0), (0,1), (3,5)), ((0,0), (1,5))))
    
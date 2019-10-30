import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def move(arr, x, y, N):
    global result
    if result != 1:
        for i in range(4):
            if [x + dx[i], y + dy[i]] not in memoization:
                if x + dx[i] in range(N) and y + dy[i] in range(N):
                    if arr[x+dx[i]][y+dy[i]] == '0':
                        memoization.append([x+dx[i],y+dy[i]])
                        move(arr, x+dx[i], y+dy[i], N)
                    elif arr[x+dx[i]][y+dy[i]] == '3':
                        result = 1



for T in range(int(input())):
    result = 0
    maze = []
    memoization = []
    N = int(input())
    for i in range(N):
        maze.append(list(input()))
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                memoization.append([i, j])
                maze[i][j] = '0'
                break
        if memoization:
            break
    move(maze, memoization[0][0], memoization[0][1], N)
    print('#{} {}'.format(T+1, result))


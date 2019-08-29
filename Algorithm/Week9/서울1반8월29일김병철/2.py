direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

# def bfs(location):
#     global T
#     global N
#     global maze
#     depth = 0
#     visited = []
#     queue = [location]
#     last = location
#     while queue:
#         a = queue.pop(0)
#         visited.append(a)
#         if maze[a[0]][a[1]] == 3:
#             print('#{} {}'.format(T + 1, depth-1))
#             return
#         for i in range(4):
#             temp = [a[0] + direction[i][0], a[1] + direction[i][1]]
#             if temp[0] in range(N) and temp[1] in range(N):
#                 if maze[temp[0]][temp[1]] != 1:
#                     if temp not in visited:
#                         queue.append(temp)
#                         b = temp
#         if a == last:
#             last = b
#             depth += 1
#
#     print('#{} {}'.format(T + 1,  0))

for T in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for i in range(N)]
    def ss():
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                if maze[i][j] == 2:
                    return (i, j)
    # bfs(start)
    start = ss()
    depth = 0
    visited = {}
    queue = [start]
    last = start
    end = False
    while queue:
        a = queue.pop(0)
        visited[a] = 1
        if maze[a[0]][a[1]] == 3:
            print('#{} {}'.format(T + 1, depth - 1))
            end = True
            break
        for dx, dy in direction:
            temp = (a[0] + dx, a[1] + dy)
            if 0 <= temp[0] < N and 0 <= temp[1] < N:
                if maze[temp[0]][temp[1]] != 1:
                    if not visited.get(temp):
                        queue.append(temp)
                        b = temp
        if a == last:
            last = b
            depth += 1
    if not end:
        print('#{} {}'.format(T + 1, 0))
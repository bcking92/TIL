from time import time

a = time()

def is_splited(arr, N, M):
    temp = [[] for i in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i].append(arr[i][j])
    part = 0
    while True:
        stack = []
        for i in range(N):
            for j in range(M):
                if temp[i][j]:
                    start = i, j
                    stack.append(start)
                    break
            if stack:
                break
        else:
            return False
        while stack:
            p = stack.pop()
            temp[p[0]][p[1]] = 0
            for j in range(4):
                temp_x = p[0] + direction[j][0]
                temp_y = p[1] + direction[j][1]
                if 0 <= temp_x < N and 0 <= temp_y < M:
                    if temp[temp_x][temp_y]:
                        stack.append((temp_x, temp_y))
        part += 1
        if part >= 2:
            return True
        for i in temp:
            if sum(i):
               break
        else:
            return False

direction = ((0, -1), (0, 1), (1, 0), (-1, 0))
N, M = map(int, input().split())
ice_burg = [list(map(int, input().split())) for i in range(N)]
years = 0
while True:
    years += 1
    temp = [[] for i in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i].append(ice_burg[i][j])

    # for i in range(N):
    #     for j in range(M):
    #         if ice_burg[i][j]:
    #             cnt = 0
    #             for k in range(4):
    #                 temp_i = i + direction[k][0]
    #                 temp_j = j + direction[k][1]
    #                 if 0 <= temp_i < N and 0 <= temp_j < M:
    #                     if ice_burg[temp_i][temp_j] == 0:
    #                         cnt += 1
    #             temp[i][j] -= cnt
    #             if temp[i][j] < 0:
    #                 temp[i][j] = 0
    ice_burg = temp
    if is_splited(temp, N, M):
        print(years)
        break
    for i in range(N):
        if sum(ice_burg[i]):
            break
    else:
        print(0)
        break

print(time() - a)


arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]
num = 5
snail = []
for i in range(num):
    snail.append([0, 0, 0, 0, 0])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
idx = 0
min_x, min_y = 0, 0

for repeat in range(num*num):
    temp_min = 100
    for i in range(num):
        for j in range(num):
            if arr[i][j] < temp_min:
                temp_min = arr[i][j]
                min_x, min_y = i, j

    arr[min_x][min_y] = 100

    snail[x][y] = temp_min

    if x+dx[idx] not in range(num) or y+dy[idx] not in range(num):
        idx += 1
        idx %= 4
    else:
        if snail[x+dx[idx]][y+dy[idx]]:
            idx += 1
            idx %= 4

    x += dx[idx]
    y += dy[idx]

print(snail)

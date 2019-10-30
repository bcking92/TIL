import sys

sys.stdin = open('input.txt', 'r')

direction_x = [0, 1, 0, -1]
direction_y = [1, 0, -1, 0]

location_x = 0
location_y = 0

track_x = [0]
track_y = [0]

dir_index = 0

finish = False

result = 0

N = int(input())

matrix = [[0] * N for i in range(N)]

matrix[0][0] = 1

for i in range(int(input())):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 2

L = int(input())

for i in range(L):
    if finish == False:
        time, change = input().split()
        for j in range(int(time)-result):
            result += 1
            if location_x + direction_x[dir_index] not in range(N) or location_y + direction_y[dir_index] not in range(N) or matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] == 1:
                finish = True
                break
            elif matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] == 2:
                matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] = 1
                location_x += direction_x[dir_index]
                location_y += direction_y[dir_index]
                track_x.append(location_x)
                track_y.append(location_y)
            else:
                matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] = 1
                location_x += direction_x[dir_index]
                location_y += direction_y[dir_index]
                matrix[location_x][location_y] = 1
                matrix[track_x[0]][track_y[0]] = 0
                del track_x[0]
                del track_y[0]
                track_x.append(location_x)
                track_y.append(location_y)

        if finish == False:
            if change == 'D':
                dir_index += 1
                if dir_index > 3:
                    dir_index -= 4
            else:
                dir_index -= 1
                if dir_index < 0:
                    dir_index += 4
    else:
        break
while True:
    if finish:
        break
    else:
        result += 1
        if location_x + direction_x[dir_index] not in range(N) or location_y + direction_y[dir_index] not in range(N) or matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] == 1:
            finish == True
            break
        elif matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] == 2:
            matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] = 1
            location_x += direction_x[dir_index]
            location_y += direction_y[dir_index]
            track_x.append(location_x)
            track_y.append(location_y)
        else:
            matrix[location_x + direction_x[dir_index]][location_y + direction_y[dir_index]] = 1
            location_x += direction_x[dir_index]
            location_y += direction_y[dir_index]
            matrix[location_x][location_y] = 1
            matrix[track_x[0]][track_y[0]] = 0
            del track_x[0]
            del track_y[0]
            track_x.append(location_x)
            track_y.append(location_y)

print(result)




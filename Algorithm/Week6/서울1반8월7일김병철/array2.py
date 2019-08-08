my_list = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
           ]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
my_sum = 0
for x in range(len(my_list)):
    for y in range(len(my_list[0])):
        for k in range(4):
            temp_x = x + dx[k]
            temp_y = y + dy[k]
            if temp_x in range(len(my_list)) and temp_y in range(len(my_list)):
                my_sum += abs(my_list[x][y] - my_list[temp_x][temp_y])
print(my_sum)
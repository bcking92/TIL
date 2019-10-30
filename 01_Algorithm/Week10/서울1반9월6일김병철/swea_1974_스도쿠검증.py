for T in range(int(input())):
    sdoku = []
    flag = 1
    for i in range(9):
        sdoku.append(list(map(int, input().split())))
    sdoku2 = list(zip(*sdoku))
    for i in range(9):
        if set(sdoku[i]) != {1,2,3,4,5,6,7,8,9} or set(sdoku2[i]) != {1,2,3,4,5,6,7,8,9}:
            flag = 0
            break
    if flag:
        for i in range(0,9,3):
            for j in range(0,9,3):
                if {sdoku[i][j], sdoku[i][j+1], sdoku[i][j+2], sdoku[i+1][j], sdoku[i+1][j+1], sdoku[i+1][j+2], sdoku[i+2][j], sdoku[i+2][j+1], sdoku[i+2][j+2]} != {1,2,3,4,5,6,7,8,9}:
                    flag = 0
                    break
            if not flag:
                break
    if flag:
        print('#{} {}'.format(T + 1, 1))
    else:
        print('#{} {}'.format(T + 1, 0))



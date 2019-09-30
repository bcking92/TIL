su_list = [[i,True] for i in range(10 ** 6)]

for i in range(2, 10 ** 6):
    if su_list[i][1] == True:
        print(su_list[i][0], end = ' ')
        for j in range(i, 10 ** 6, i):
            su_list[j][1] = False
test = int(input())
for i in range(test):
    A = False
    B = False
    C = False
    sdoku = []
    for j in range(9):
        sdoku.append(input())
    for z in range(9):
        if len(set(sdoku[z])) == 10:
            continue
        else:
            break
    else:
        A = True
        for k in range(3):
            if len(set(sdoku[0+3*k][0:5]) & set(sdoku[1+3*k][0:5])) == 1 and len(set(sdoku[1+3*k][0:5]) & set(sdoku[2+3*k][0:5])) == 1 and len(set(sdoku[0+3*k][0:5]) & set(sdoku[2+3*k][0:5])) == 1:
                if len(set(sdoku[0+3*k][5:11]) & set(sdoku[1+3*k][5:11])) == 1 and len(set(sdoku[1+3*k][5:11]) & set(sdoku[2+3*k][5:11])) == 1 and len(set(sdoku[0+3*k][5:11]) & set(sdoku[2+3*k][5:11])) == 1:
                    if len(set(sdoku[0+3*k][12:]) & set(sdoku[1+3*k][12:])) == 1 and len(set(sdoku[1+3*k][12:]) & set(sdoku[2+3*k][12:])) == 1 and len(set(sdoku[0+3*k][12:]) & set(sdoku[2+3*k][12:])) == 1:
                        continue
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            B = True
            for h in range(0,17,2):
                if len(set(sdoku[0][0+h]+sdoku[1][0+h]+sdoku[2][0+h]+sdoku[3][0+h]+sdoku[4][0+h]+sdoku[5][0+h]+sdoku[6][0+h]+sdoku[7][0+h]+sdoku[8][0+h])) == 9:
                    continue
                else:
                    break
            else:
                C = True
    if A and B and C:
        print('#{0} 1'.format(i+1))
    else:
        print('#{0} 0'.format(i+1))


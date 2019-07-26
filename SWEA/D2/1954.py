a = int(input())
for s in range(a):
    n = int(input())
    snail = list()
    num = '*'*n
    for i in range(n):
        snail.append(list(num))
    loop = 1
    stage = 0
    j = 0
    for i in range(n**2):
        if loop == 1:
            top = n-2*stage - 1
            snail[stage][j+stage]= i+1
            if j == top:
                loop += 1
                j = 0
            else:
                j += 1
        elif loop == 2:
            top = n-2*stage - 1
            snail[j+1+stage][n-stage-1] = i + 1
            if j == top - 1:
                loop += 1
                j = 0
            else:
                j += 1
        elif loop == 3:
            top = n-2*stage - 1
            snail[n-stage-1][n-stage-2-j] = i + 1
            if j == top - 1:
                loop += 1
                j = 0
            else:
                j += 1
        else:
            top = n-2*stage - 1
            snail[n-stage-2-j][stage] = i + 1
            if j == top - 2:
                loop = 1
                j = 0
                stage += 1
            else:
                j += 1
    print('#{0}'.format(s+1))
    for i in range(n):
        print(str(snail[i]).strip(']').strip('[').replace(',',''))
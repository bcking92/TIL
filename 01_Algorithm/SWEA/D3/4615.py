import sys

sys.stdin = open('input.txt','r')

def iswall(x, y,N):
    if x not in range(N) or y not in range(N):
        return False
    else:
        return True

dir_x = [0, 0, 1, -1, 1, -1, 1, -1]
dir_y = [1, -1, 0, 0, 1, -1, -1, 1]

for i in range(int(input())):
    N, M = map(int, input().split())
    osel = []
    for j in range(N):
        a = []
        for k in range(N):
            a.append(0)
        osel.append(a)

    osel[int(N / 2) - 1][int(N / 2) - 1] = 2
    osel[int(N / 2) - 1][int(N / 2)] = 1
    osel[int(N / 2)][int(N / 2) - 1] = 1
    osel[int(N / 2)][int(N / 2)] = 2

    for j in range(M):
        y, x, doll = map(int, input().split())
        x -= 1
        y -= 1
        osel[x][y] = doll
        for k in range(8):
            index = k
            temp = 1
            while iswall(x + temp * dir_x[index], y + temp * dir_y[index], N) and osel[x + temp * dir_x[index]][y + temp * dir_y[index]]:
                if osel[x + temp * dir_x[index]][y + temp * dir_y[index]] == doll :
                    for l in range(1,temp):
                        osel[x + l * dir_x[index]][y + l * dir_y[index]] = doll
                    break
                temp += 1

    cnt_black = 0
    cnt_white = 0
    for j in range(N):
        for k in range(N):
            if osel[j][k] == 1:
                cnt_black += 1
            elif osel[j][k] == 2:
                cnt_white += 1
            else:
                continue

    print('#{} {} {}'.format(i+1,cnt_black,cnt_white))



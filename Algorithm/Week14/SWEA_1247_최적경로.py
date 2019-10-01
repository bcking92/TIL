# -*- coding: utf-8 -*-

def permi():
    global 방문, 임시, 결과, 현재최소
    if 결과 < 현재최소:
        if sum(방문) == N:
            # print(임시)
            결과 += 인접행렬[임시[-1]][-1]
            # print(결과)
            if 결과 < 현재최소:
                현재최소 = 결과
            결과 -= 인접행렬[임시[-1]][-1]
        else:
            for i in range(N):
                if not 방문[i]:
                    if not sum(방문):
                        방문[i] = 1
                        임시.append(i + 1)
                        결과 += 인접행렬[0][임시[0]]
                        permi()
                        결과 -= 인접행렬[0][임시[0]]
                        임시.pop()
                        방문[i] = 0
                    else:
                        방문[i] = 1
                        임시.append(i + 1)
                        결과 += 인접행렬[임시[sum(방문) - 2]][임시[sum(방문) - 1]]
                        permi()
                        결과 -= 인접행렬[임시[sum(방문) - 2]][임시[sum(방문) - 1]]
                        임시.pop()
                        방문[i] = 0

for T in range(int(input())):
    N = int(input())
    배열 = list(map(int, input().split()))
    방문 = [0] * N
    좌표 = []
    임시 = []
    결과 = 0
    현재최소 = 1000
    for i in range(0, (2 + N) * 2, 2):
        좌표.append((배열[i], 배열[i + 1]))
    좌표 = 좌표[:1] + sorted(좌표[2:]) + 좌표[1:2]
    # print(좌표)
    인접행렬 = [[0] * (N + 2) for i in range(N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            인접행렬[i][j] = abs(좌표[i][0] - 좌표[j][0]) + abs(좌표[i][1] - 좌표[j][1])
    permi()
    print('#{} {}'.format(T + 1, 현재최소))
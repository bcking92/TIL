for T in range(int(input())):
    N, M = map(int, input().split())
    fly = []
    result = 0
    for i in range(N):
        fly.append(tuple(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += sum(fly[i+k][j:j+M])
            if result < temp:
                result = temp
    print('#{} {}'.format(T + 1, result))
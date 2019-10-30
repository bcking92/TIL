for T in range(int(input())):
    N, K = map(int, input().split())
    result = 0
    board1 = []
    for i in range(N):
        board1.append(tuple(input().split()))
    board2 = tuple(zip(*board1))

    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if board1[i][j] == '1':
                cnt1 += 1
            else:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            if board2[i][j] == '1':
                cnt2 += 1
            else:
                if cnt2 == K:
                    result += 1
                cnt2 = 0
        if cnt1 == K:
            result += 1
        if cnt2 == K:
            result += 1
    print('#{} {}'.format(T + 1, result))

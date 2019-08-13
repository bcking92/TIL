for i in range(int(input())):
    N, M, K = map(int,input().split())
    exp = sorted(list(map(int,input().split())))
    stock = K
    for j in exp:
        if M > j:
            print('#{} Impossible'.format(i+1))
            break
    else:
        for k in range(int(max(exp)/M)):
            a = sum(1 for c in exp if M*(k+1) <= c < M*(k+2))
            if a > stock:
                print('#{} Impossible'.format(i+1))
                break
            else:
                stock += K - a
        else:
            print('#{} Possible'.format(i+1))
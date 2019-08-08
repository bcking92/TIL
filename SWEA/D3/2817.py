for i in range(int(input())):
    N, K = map(int,input().split())
    l = list(map(int,input().split()))
    r = 0
    for j in range(1,1<<N):
        s = 0
        for k in range(N):
            if j & (1<<k): s += l[k]
            if s > K: break
        if s == K: r += 1
    print('#{} {}'.format(i+1,r))


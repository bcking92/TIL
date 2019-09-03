for T in range(int(input())):
    N, M, L = map(int, input().split())
    arr = list(map(int,input().split()))
    for i in range(M):
        idx, v = map(int, input().split())
        arr.insert(idx, v)
    print('#{} {}'.format(T + 1, arr[L]))
for T in range(int(input())):
    N, M, L = map(int, input().split())
    arr = [0 for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b
    for i in range(len(arr)-1, 0, -1):
        if arr[i]:
            arr[i//2] += arr[i]
    print('#{} {}'.format(T+1, arr[L]))
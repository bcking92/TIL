for T in range(int(input())):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    now = 0

    for i in range(K):
        now += M
        if now > len(arr):
            now -= len(arr)
            arr.insert(now, arr[now] + arr[now - 1])
        elif now == len(arr):
            arr.append(arr[now] + arr[0])

    print('#{} {}'.format(T + 1, ' '.join(map(str, arr[::-1]))))

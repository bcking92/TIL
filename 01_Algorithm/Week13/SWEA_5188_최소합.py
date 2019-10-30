def search(arr, start, end, temp):
    global candi, now_min
    if temp < now_min:
        if start == end:
            if temp < now_min:
                now_min = temp
                candi.append(temp)
        else:
            if start[0] + 1 < N:
                search(arr, (start[0] + 1, start[1]), end, temp + arr[start[0] + 1][start[1]])
            if start[1] + 1 < N:
                search(arr, (start[0], start[1] + 1), end, temp + arr[start[0]][start[1] + 1])

for T in range(int(input())):
    N = int(input())
    arr = [tuple(map(int, input().split())) for i in range(N)]
    candi = []
    now_min = 1000000
    search(arr, (0, 0), (N-1, N-1), arr[0][0])
    print('#{} {}'.format(T + 1, min(candi)))